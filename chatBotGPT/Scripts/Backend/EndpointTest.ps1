function Test-AnalyzeEndpoint {
    param (
        [Parameter(Mandatory=$true)]
        [string]$TextInput
    )
    $uri = "http://localhost:5000/analyze"

    $body = @{
        text = $TextInput
    } | ConvertTo-Json

    $response = Invoke-RestMethod -Uri $Uri -Method Post -Body $body -ContentType "application/json"

    Write-Host $response.result -ForegroundColor Green

    Write-Host "---" -ForegroundColor Red
}

Test-AnalyzeEndpoint -TextInput "Hello, how are you?"
Test-AnalyzeEndpoint -TextInput "What is an API?"
Test-AnalyzeEndpoint -TextInput "Tell me more about REST API?"
