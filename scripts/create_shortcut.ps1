try {
    # Get the script directory and project root
    $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
    $projectRoot = Resolve-Path "$scriptDir\.."

    # Convert PathInfo to string using .Path
    $exePath = (Resolve-Path "$projectRoot\dist\gui.exe").Path
    $iconPath = (Resolve-Path "$projectRoot\icone.ico").Path

    # Check if both files exist
    if (-not (Test-Path $exePath)) { throw "Executable not found at $exePath" }
    if (-not (Test-Path $iconPath)) { throw "Icon not found at $iconPath" }

    # Define desktop path and shortcut location
    $desktopPath = [Environment]::GetFolderPath("Desktop")
    $shortcutPath = Join-Path $desktopPath "PDFtoDOCX Converter.lnk"

    # Create the shortcut using WScript.Shell
    $WScriptShell = New-Object -ComObject WScript.Shell
    $shortcut = $WScriptShell.CreateShortcut($shortcutPath)
    $shortcut.TargetPath = $exePath
    $shortcut.WorkingDirectory = Split-Path $exePath
    $shortcut.IconLocation = "$iconPath,0"
    $shortcut.WindowStyle = 1
    $shortcut.Save()

    Write-Host "✅ Shortcut created successfully on your Desktop."
} catch {
    Write-Host "❌ Failed to create the shortcut. Details:" -ForegroundColor Red
    Write-Host $_.Exception.Message
}

