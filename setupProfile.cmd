@REM This script is for windows machine only
@REM It will create profile folder and it will start chrome browser
@REM Change "customProfilesFolderName" and "newProfileName" as per need

@echo.
@echo Creation of new profile started...
@echo.

@set customProfilesFolderName=CustomProfiles
@set newProfileName=Profile 1

@set customProfilesPath=%LocalAppData%\Google\Chrome\User Data\%customProfilesFolderName%

@set chromeExePath=%ProgramFiles%\Google\Chrome\Application\chrome.exe

@REM Create profile folders
@mkdir "%customProfilesPath%\%newProfileName%"
@echo New profile-%newProfileName% folder created

@set runCommand="%chromeExePath%" --user-data-dir="%customProfilesPath%" --profile-directory="%newProfileName%"
%runCommand%

@echo.
@echo Set below as Target in chrome shortcut properties
@echo %runCommand%

@echo.
@echo Creation of new profile ended.
@echo.