@echo off
call _internal\setenv.bat

"%PYTHON_EXECUTABLE%" -m pip install cmake
"%PYTHON_EXECUTABLE%" -m pip install https://files.pythonhosted.org/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#sha256=794994fa2c54e7776659fddb148363a5556468a6d5d46be8dad311722d54bfcf
"%PYTHON_EXECUTABLE%" -m pip install face_recognition

move facematch.py "%DFL_ROOT%"

(goto) 2>nul & del "%~f0"