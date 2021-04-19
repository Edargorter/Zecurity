$file = "something.txt"
$content = get-content $file -Encoding Byte
$encoded  = [System.Convert]::ToBase64String($content)
Write-Host "File encoded in base64: " $file 
Write-Host "Time: " Get-Date
$encoded > $file.encoded

#[IO.file]::WriteAllBytes($filename + ".encoded", $bytes)
