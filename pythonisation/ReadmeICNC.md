~/w/work/prestation1/acxys-main/acxys-plasma-gui-cartesian/AlgoXYZ/src
5 fonctions sont definies
1. void LoadDLL(void);
2. int Connect(void);
3. void GetSysInfo(void);
4. void CheckStatus(void);
5. int MachineOrigine(void);
seule GetSysInfo() est utilisee, c'est dans ExecuteMicroTrajectoire.cpp
en revanche les fonctions _ICNC_xxxxx sont utilisees.


~/w/work/prestation1/acxys-main/acxys-plasma-gui-cartesian/src
16 fonctions sont utilisees
_ICNC_Connect
_ICNC_ErrorReset
_ICNC_GetBoardStatus
_ICNC_GetBufferStatus
_ICNC_GetInput
_ICNC_GetOutputAll
_ICNC_MachineHome
_ICNC_MoveProfileAbsBuf
_ICNC_MoveSpeedAbsBuf
_ICNC_SetOutput
_ICNC_SetOutputBuf
_ICNC_SetSimulationMode
_ICNC_SlowStopAllAndClear
_ICNC_WaitBuf
_ICNC_WriteParameter
_ICNC_WriteUserMem


liste des appels:
acquitdefault.cpp
        _ICNC_SetOutput(4, TRUE);
                _ICNC_SetOutput(4, FALSE);
boardspecs.cpp
        DWORD version = _ICNC_GetDLLVersion();
        _ICNC_GetSysInfo(
cartesianwindow.cpp
                _ICNC_WriteParameter(EE_XSENS, axisData.m_sensX, TRUE, 1000);
                _ICNC_WriteParameter(EE_YSENS, axisData.m_sensY, TRUE, 1000);
                _ICNC_WriteParameter(EE_ZSENS, axisData.m_sensZ, TRUE, 1000);
                _ICNC_WriteParameter(EE_MAX_COURSE_X, axisData.m_courseX, TRUE, 1000);
                _ICNC_WriteParameter(EE_MAX_COURSE_Y, axisData.m_courseY, TRUE, 1000);
                _ICNC_WriteParameter(EE_MAX_COURSE_Z, axisData.m_courseZ, TRUE, 1000);
                _ICNC_WriteParameter(EE_DEFAULT_ACCEL, axisData.m_accelerationDefaut, TRUE, 1000);
                _ICNC_WriteParameter(EE_DEFAULT_STARTF, axisData.m_frequenceDefaut, TRUE, 1000);
                _ICNC_WriteParameter(EE_FDC_ORIGINEX, axisData.m_numCapteurPomX, TRUE, 1000);
                _ICNC_WriteParameter(EE_FDC_ORIGINEY, axisData.m_numCapteurPomY, TRUE, 1000);
                _ICNC_WriteParameter(EE_FDC_ORIGINEZ, axisData.m_numCapteurPomZ, TRUE, 1000);
                _ICNC_WriteParameter(EE_ORIGINE_XSENS, axisData.m_sensPomX, TRUE, 1000);
                _ICNC_WriteParameter(EE_ORIGINE_YSENS, axisData.m_sensPomY, TRUE, 1000);
                _ICNC_WriteParameter(EE_ORIGINE_ZSENS, axisData.m_sensPomZ, TRUE, 1000);
                        _ICNC_WriteParameter(EE_ORIGINE_SPEED_RAPIDE, vitesse, TRUE, 1000);
                        _ICNC_WriteParameter(EE_ORIGINE_SPEED_RAPIDEY, vitesse, TRUE, 1000);
                        _ICNC_WriteParameter(EE_ORIGINE_SPEED_RAPIDEZ, vitesse, TRUE, 1000);
                _ICNC_WriteUserMem(0, axisData.m_tempsReponsePlasma);
        _ICNC_Disconnect();
        bool connected = _ICNC_Connect(0);
        if (_ICNC_ErrorReset(ICNC_STATUS_BIT_LOCKED) != ICNCUSB_SUCCESS)
        if (_ICNC_ErrorReset(ICNC_STATUS_BIT_EMERGENCYSTOP | ICNC_STATUS_BIT_LOCKED | ICNC_STATUS_BIT_STROKE_LIMIT | ICNC_STATUS_BIT_HOMING_ERROR) != ICNCUSB_SUCCESS) {
        if (_ICNC_GetBoardStatus(ICNC_STATUS_BOARD_STATUS, &statusBoard) != ICNCUSB_SUCCESS) {
                if (_ICNC_MachineHome(Axis, 0x7FFFFFFF, 0x7FFFFFFF, 0x7FFFFFFF, 0x7FFFFFFF, 0x7FFFFFFF) != ICNCUSB_SUCCESS)
        return  _ICNC_MoveProfileAbsAsync(ICNC_AXE_X, FStartStop, Accel, stepSpeed, Decel, stepPosition);
        return  _ICNC_MoveProfileAbsAsync(ICNC_AXE_Y, FStartStop, Accel, stepSpeed, Decel, stepPosition);
        return  _ICNC_MoveProfileAbsAsync(ICNC_AXE_Z, FStartStop, Accel, stepSpeed, Decel, stepPosition);
        if (_ICNC_SlowStopMotors(ICNC_AXE_X | ICNC_AXE_Y | ICNC_AXE_Z) != ICNCUSB_SUCCESS)
                if (_ICNC_ErrorReset(ICNC_STATUS_BIT_LOCKED) != ICNCUSB_SUCCESS)
        if (_ICNC_GetBoardStatus(ICNC_STATUS_BOARD_STATUS | ICNC_STATUS_BUFFER_FREE | ICNC_STATUS_ACTUALX | ICNC_STATUS_ACTUALY
                _ICNC_GetInput(6, &machineButton);
                _ICNC_GetInput(5, &driverDefault);
executetrajectory.cpp
                _ICNC_SetOutput(4, TRUE);
                        _ICNC_SetOutput(4, FALSE);
main.cpp
        DWORD simul = _ICNC_SetSimulationMode(true);
        DWORD simul = _ICNC_SetSimulationMode(false);
plasmacommands.cpp
                _ICNC_SetOutput(2, TRUE);
                _ICNC_SetOutput(2, FALSE);
