$file = "underperforming_employees.pdf"
$content = get-content $file -Encoding Byte
#$bytes = [System.Text.Encoding]::UTF8.GetBytes($content)
$encoded = [System.Convert]::ToBase64String($content)
Write-Host "Encoded: " $encoded 
$encoded > temp.txt
#$file = "temp.txt"
#$encoded = get-content $file

#$bytes = [System.Convert]::FromBase64String($encoded)
#[IO.file]::WriteAllBytes("decoded.pdf", $bytes)
#$bytes = [System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($encoded)) | Out-File -Encoding ASCII decoded.pdf
#[system.io.file]::WriteAllBytes('decoded.pdf', $bytes)
