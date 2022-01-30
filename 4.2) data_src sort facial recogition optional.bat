@echo off
call _internal\setenv.bat


ECHO This script helps you sort through your "aligned" faces by asking you to provide the
ECHO name of one of the existing files to use as a refernce. It uses that face to find
ECHO any other matching faces in the "aligned" folder. It moves any matches it finds into
ECHO a "matches" folder inside the "aligned" folder. You should verify that it didn't miss
ECHO any valid faces by manually moving them into the "matches" folder, delete any remaining
ECHO faces or bad images, and move the contents of the "matches" folder back into the
ECHO "aligned" folder, leaving onlly matching faces.
ECHO.
ECHO. This is the data_src directory version.
ECHO.
ECHO.


:getFullPath
ECHO Which file would you like to use as the reference face to find matches for? (e.g. 0000.jpg)
set /p referenceFile=Enter file name: 

rem set fullPath=%WORKSPACE%\data_src\aligned\%referenceFile%

pushd .
cd %WORKSPACE%\data_src\aligned
set data_srcAlignedDir=%CD%
set fullPath=%data_srcAlignedDir%\%referenceFile%
popd

if NOT exist %fullPath% (
	echo.
	echo %fullPath% is not a valid file
	echo Please specify a valid file
	pause
	goto :getFullPath
) else (
	echo Found %fullPath%
	echo Begining face matching.
	"%PYTHON_EXECUTABLE%" "%DFL_ROOT%"\facematch.py %fullPath% %data_srcAlignedDir%
	echo.
)

pause