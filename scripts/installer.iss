[Setup]
AppName=PrivateDocs AI Feasibility
AppVersion=0.1.0
DefaultDirName={localappdata}\PrivateDocsAI-Feasibility
PrivilegesRequired=lowest
OutputDir=..\dist
OutputBaseFilename=PrivateDocsAI-Feasibility-Setup
Compression=lzma2/fast
SolidCompression=yes
Uninstallable=yes
[Files]
Source: "..\dist\PrivateDocsAI\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
[Icons]
Name: "{userprograms}\PrivateDocs AI Feasibility"; Filename: "{app}\PrivateDocsAI.exe"
