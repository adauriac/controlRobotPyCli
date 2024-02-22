import ctypes,sys

"""
appel depuis msys2:
  /C/Users/ACXYS/Downloads/python-3.12.1-embed-win32/python -i ICNC2.py
  ou
  python32 ICNC2.py
appel depuis powershell:
  C:\\Users\\ACXYS\\Downloads\\python-3.12.1-embed-win32\\python.exe  -i .\\ICNC2.py
"""

class ICNC2:
	EVENT_MANUALCONTROL  = 0
	EVENT_STARTPROCESS   = 1
	EVENT_RAPIDTOXY      = 2
	EVENT_TOOLDOWN       = 3
	EVENT_DRILLING       = 4
	EVENT_FEEDING        = 5
	EVENT_LIFTUP         = 6
	EVENT_PARKTOOL       = 7
	EVENT_ENDPROCESS     = 8
	EVENT_BREAKPROCESS   = 0xFFFF
	ICNC_CONST_MAX_READ_EEPROM_SIZE = 62
	ICNC_CONST_MAX_WRITE_EEPROM_SIZE = 57
	ICNC_AXE_NONE = 0
	ICNC_AXE_X = 0x01
	ICNC_AXE_Y = 0x02
	ICNC_AXE_YX = 0x03
	ICNC_AXE_Z = 0x04
	ICNC_AXE_ZX = 0x05
	ICNC_AXE_ZY = 0x06
	ICNC_AXE_ZYX = 0x07
	ICNC_AXE_A = 0x08
	ICNC_AXE_AX = 0x09
	ICNC_AXE_AY = 0x0A
	ICNC_AXE_AYX = 0x0B
	ICNC_AXE_AZ = 0x0C
	ICNC_AXE_AZX = 0x0D
	ICNC_AXE_AZY = 0x0E
	ICNC_AXE_AZYX = 0x0F
	ICNC_AXE_B = 0x10
	ICNC_AXE_BX = 0x11
	ICNC_AXE_BY = 0x12
	ICNC_AXE_BYX = 0x13
	ICNC_AXE_BZ = 0x14
	ICNC_AXE_BZX = 0x15
	ICNC_AXE_BZY = 0x16
	ICNC_AXE_BZYX = 0x17
	ICNC_AXE_BA = 0x18
	ICNC_AXE_BAX = 0x19
	ICNC_AXE_BAY = 0x1A
	ICNC_AXE_BAYX = 0x1B
	ICNC_AXE_BAZ = 0x1C
	ICNC_AXE_BAZX = 0x1D
	ICNC_AXE_BAZY = 0x1E
	ICNC_AXE_BAZYX = 0x1F
	ICNC_ANALOG1 = 0x01
	ICNC_ANALOG2 = 0x02
	ICNC_ANALOG3 = 0x03
	ICNC_ANALOG4 = 0x04
	ICNC_CONST_OVERRIDE_PROG = 0
	ICNC_CONST_OVERRIDE_ANA1 = 1
	ICNC_CONST_OVERRIDE_ANA2 = 2
	ICNC_CONST_OVERRIDE_ANA3 = 3
	ICNC_CONST_OVERRIDE_ANA4 = 4
	ICNC_STATUS_BOARD_STATUS = 0x00000001
	ICNC_STATUS_BUFFER_FREE = 0x00000002
	ICNC_STATUS_ACTUALX = 0x00000004
	ICNC_STATUS_ACTUALY = 0x00000008
	ICNC_STATUS_ACTUALZ = 0x00000010
	ICNC_STATUS_ACTUALA = 0x00000020
	ICNC_STATUS_ACTUALB = 0x00000040
	ICNC_STATUS_INPUT = 0x00000080
	ICNC_STATUS_LAST_PROBE = 0x00000100
	ICNC_STATUS_ANALOG_IN1 = 0x00000200
	ICNC_STATUS_ANALOG_IN2 = 0x00000400
	ICNC_STATUS_ANALOG_IN3 = 0x00000800
	ICNC_STATUS_ANALOG_IN4 = 0x00001000
	ICNC_STATUS_THC_TARGET = 0x00002000
	ICNC_STATUS_MATRIX_KEY = 0x00004000
	ICNC_STATUS_ENCODER = 0x00008000
	ICNC_STATUS_A_PULSES_COUNTER = 0x00010000
	ICNC_STATUS_B_PULSES_COUNTER = 0x00020000
	ICNC_STATUS_A_PULSES_FREQUENCY = 0x00040000
	ICNC_STATUS_B_PULSES_FREQUENCY = 0x00080000
	ICNC_STATUS_ANALOG_AOUT1 = 0
	ICNC_STATUS_ANALOG_AOUT2 = 0x00200000
	ICNC_STATUS_BOARD_STATUS2 = 0x00400000
	ICNC_STATUS_BIT_XMOVING = 0x00000001
	ICNC_STATUS_BIT_YMOVING = 0x00000002
	ICNC_STATUS_BIT_ZMOVING = 0x00000004
	ICNC_STATUS_BIT_AMOVING = 0x00000008
	ICNC_STATUS_BIT_BMOVING = 0x00000010
	ICNC_STATUS_BIT_BUFFER_EMPTY = 0x00000020
	ICNC_STATUS_BIT_BUFFER_FREZED = 0x00000040
	ICNC_STATUS_BIT_EMERGENCYSTOP = 0x00000080
	ICNC_STATUS_BIT_LOCKED = 0x00000100
	ICNC_STATUS_BIT_STROKE_LIMIT = 0x00000200
	ICNC_STATUS_BIT_HOMING = 0x00000400
	ICNC_STATUS_BIT_HOMING_ERROR = 0x00000800
	ICNC_STATUS_BIT_PROBING = 0x00001000
	ICNC_STATUS_BIT_PROBING_ERROR = 0x00002000
	ICNC_STATUS_BIT_EEWRITE_INPROGRESS = 0x00004000
	ICNC_STATUS_BIT_EEWRITE_ERROR = 0x00008000
	ICNC_STATUS_BIT_PROMPT_STATE = 0x00010000
	ICNC_STATUS_BIT_OVERRIDE = 0x00020000
	ICNC_STATUS_BIT_OVERRIDE_ALLOWED = 0x00040000
	ICNC_STATUS_BIT_WAIT_INPUT = 0x00080000
	ICNC_STATUS_BIT_WAIT_INPUT_ERROR = 0x00100000
	ICNC_STATUS_BIT_THC_ACTIVATED = 0x00200000
	ICNC_STATUS_BIT_X_ASYNC_MOVING = 0x00400000
	ICNC_STATUS_BIT_Y_ASYNC_MOVING = 0x00800000
	ICNC_STATUS_BIT_Z_ASYNC_MOVING = 0x01000000
	ICNC_STATUS_BIT_A_ASYNC_MOVING = 0x02000000
	ICNC_STATUS_BIT_B_ASYNC_MOVING = 0x04000000
	ICNC_STATUS_BIT_X_LIMIT = 0x08000000
	ICNC_STATUS_BIT_Y_LIMIT = 0x10000000
	ICNC_STATUS_BIT_Z_LIMIT = 0x20000000
	ICNC_STATUS_BIT_A_LIMIT = 0x40000000
	ICNC_STATUS_BIT_B_LIMIT = 0x80000000
	ICNC_STATUS2_BIT_XDIRECTION = 0x00000001
	ICNC_STATUS2_BIT_YDIRECTION = 0x00000002
	ICNC_STATUS2_BIT_ZDIRECTION = 0x00000004
	ICNC_STATUS2_BIT_ADIRECTION = 0x00000008
	ICNC_STATUS2_BIT_BDIRECTION = 0x00000010
	ICNC_STATUS2_BIT_BASIC_TX_OVERRUN = 0x00000020
	ICNC_STATUS2_BIT_BASIC_RX_OVERRUN = 0x00000040
	ICNC_STATUS2_BIT_BASIC_RUNNING = 0x00000080
	ICNC_STATUS2_BIT_B8 = 0x00000100
	ICNC_STATUS2_BIT_B9 = 0x00000200
	ICNC_STATUS2_BIT_B10 = 0x00000400
	ICNC_STATUS2_BIT_B11 = 0x00000800
	ICNC_STATUS2_BIT_B12 = 0x00001000
	ICNC_STATUS2_BIT_B13 = 0x00002000
	ICNC_STATUS2_BIT_B14 = 0x00004000
	ICNC_STATUS2_BIT_B15 = 0x00008000
	ICNC_STATUS2_BIT_MB_RECEIVED = 0x00010000
	ICNC_STATUS2_BIT_MB_USR_RPM_CHANGED = 0x00020000
	ICNC_STATUS2_BIT_B18 = 0x00040000
	ICNC_STATUS2_BIT_B19 = 0x00080000
	ICNC_STATUS2_BIT_B20 = 0x00100000
	ICNC_STATUS2_BIT_B21 = 0x00200000
	ICNC_STATUS2_BIT_B22 = 0x00400000
	ICNC_STATUS2_BIT_B23 = 0x00800000
	ICNC_STATUS2_BIT_B24 = 0x01000000
	ICNC_STATUS2_BIT_B25 = 0x02000000
	ICNC_STATUS2_BIT_B26 = 0x04000000
	ICNC_STATUS2_BIT_B27 = 0x08000000
	ICNC_STATUS2_BIT_B28 = 0x10000000
	ICNC_STATUS2_BIT_B29 = 0x20000000
	ICNC_STATUS2_BIT_B30 = 0x40000000
	ICNC_STATUS2_BIT_B31 = 0x80000000
	ICNC_SYS_INFO_BUFFER_SIZE = 0x00000001
	ICNC_SYS_INFO_MAX_FREQUENCY = 0x00000002
	ICNC_SYS_INFO_APP_VERSION_H = 0x00000004
	ICNC_SYS_INFO_APP_VERSION_L = 0x00000008
	ICNC_SYS_INFO_LOADER_VERSION_H = 0x00000010
	ICNC_SYS_INFO_LOADER_VERSION_L = 0x00000020
	ICNC_SYS_INFO_BOARD_VERSION = 0x00000040
	ICNC_SYS_INFO_EEPROM_SIZE = 0x00000080
	ICNC_SYS_INFO_USR_MEM_SIZE = 0x00000100
	ICNC_SYS_INFO_AVAILABLE_AOUT = 0x00000200
	ICNC_SYS_INFO_AVAILABLE_AIN = 0x00000400
	ICNC_SYS_INFO_DAC_RESOLUTION = 0x00000800
	ICNC_SYS_INFO_ADC_RESOLUTION = 0x00001000
	ICNC_SYS_INFO_AVAILABLE_DOUT = 0x00002000
	ICNC_SYS_INFO_AVAILABLE_DIN = 0x00004000
	ICNC_CMD_MOVE_CONSTANT_REL_BUF = 1
	ICNC_CMD_MOVE_CONSTANT_ABS_BUF = 25
	ICNC_CMD_MOVE_RAMP_BUF = 2
	ICNC_CMD_RAMPUP_ABS_BUF = 3
	ICNC_CMD_RAMPDOWN_ABS_BUF = 4
	ICNC_CMD_MOVE_ARC_XY_BUF = 97
	ICNC_CMD_PROFILE_ABS_BUF = 6
	ICNC_CMD_PROFILE_REL_BUF = 7
	ICNC_CMD_FREEZE_BUF = 11
	ICNC_CMD_SET_OUTPUT_BUF = 13
	ICNC_CMD_SET_OUTPUT_ALL_BUF = 14
	ICNC_CMD_SET_ANALOG_BUF = 15
	ICNC_CMD_TEMPO_BUF = 20
	ICNC_CMD_WAIT_INPUT_BUF = 21
	ICNC_CMD_WRITE_USER_MEM_BUF = 22
	ICNC_CMD_SET_OVERRIDE_STATE_BUF = 23
	ICNC_CMD_MOVE_TO_SENSOR_BUF = 24
	ICNC_CMD_SET_THC_ONOFF_BUF = 26
	ICNC_CMD_PROBE = 40
	ICNC_CMD_BREAKE_AXES = 41
	ICNC_CMD_BREAKE_AXES_AND_CLEAR = 42
	ICNC_CMD_STOP = 43
	ICNC_CMD_GET_OUTPUT_ALL = 44
	ICNC_CMD_GET_INPUT = 45
	ICNC_CMD_GET_INPUT_ALL = 46
	ICNC_CMD_GET_ANALOG = 47
	ICNC_CMD_SET_OUTPUT_ALL = 48
	ICNC_CMD_SET_OUTPUT = 49
	ICNC_CMD_SET_ANALOG = 50
	ICNC_CMD_GET_BUFFER_STATUS = 55
	ICNC_CMD_UNFREEZE = 56
	ICNC_CMD_WAIT_UNFREEZE = 57
	ICNC_CMD_WRITE_USER_MEM = 58
	ICNC_CMD_READ_USER_MEM = 59
	ICNC_CMD_READ_EEPROM = 62
	ICNC_CMD_WRITE_EEPROM = 63
	ICNC_CMD_READ_PARAMETER = 64
	ICNC_CMD_WRITE_PARAMETER = 65
	ICNC_CMD_ERROR_RESET = 66
	ICNC_CMD_WRITE_POSITION = 67
	ICNC_CMD_GET_STATUS = 70
	ICNC_CMD_MACHINE_HOME = 71
	ICNC_CMD_SET_OVERRIDE = 72
	ICNC_CMD_GET_OVERRIDE = 73
	ICNC_CMD_SET_THC_TARGET = 74
	ICNC_CMD_CONFIG_PROMPT = 75
	ICNC_CMD_GET_SYS_INFO = 76
	ICNC_CMD_GET_KEY = 77
	ICNC_CMD_MOVE_PROFILE_ABS_ASYNC = 80
	ICNC_CMD_MOVE_PROFILE_REL_ASYNC = 81
	ICNC_CMD_CHANGE_SPEED = 96
	ICNC_CMD_BOOT_MODE = 90
	ICNC_CMD_GET_EXECTIME = 91
	ICNC_CMD_LOCK_BOARD = 92
	ICNC_PULSE_FRAME = 93
	ICNC_USB_SPEED_SELECT = 94
	ICNC_CMD_SET_WATCHDOG = 95
	ICNC_BASIC_CONTROL = 98
	ICNC_BASIC_CONTROL_GETTX = 0
	ICNC_BASIC_CONTROL_SETRX = 1
	
	def __init__(self):
		print("init")
		self.ICNC2Lib = ctypes.CDLL("./ICNC2.dll")
	       
	def GetDLLVersion(self):
	        """
	        Retourne le numero de la dll
	        """
	        return self.ICNC2Lib._ICNC_GetDLLVersion()

	def SetSimulationMode(self,SimulationModeVal):
	        """
	        Permet de passer la DLL en mode simulation sans communication physique
	        avec la carte. Il est ainsi possible de tester le programme pour ce qui est
	        des acces aux fonctions de la DLL
	        Input : True pour passer en mode simulation
	        """
	        return self.ICNC2Lib._ICNC_SetSimulationMode(SimulationModeVal)

	def Connect(self, ICNC_Number=0):
	       """
	       Initialisation de la communication avec la carte InterpCNC
	       """
	       ans = self.ICNC2Lib._ICNC_Connect(0)
	       self.connected = ans
	       return ans

	def SetUserApplicationID(self, lUserApplicationID):
	       """
	       Definition de l'ID application
	       """
	       self.notImplemented()
	       return -1

	def Disconnect(self):
	       """
	       Arret de la communication avec la carte InterpCNC
	       """
	       self.connected = 0
	       return self.ICNC2Lib._ICNC_Disconnect()

	def ErrorReset(self, ErrorBits):
	       """
	       Deverouillage carte
	       Acquittemement Arret d'urgence, Fin de course
	       Input : Bits de defauts a remettre a 0
			    ICNC_STATUS_BIT_EMERGENCYSTOP
			    ICNC_STATUS_BIT_LOCKED
			    ICNC_STATUS_BIT_HOMING_ERROR
			    ICNC_STATUS_BIT_PROBING_ERROR
			    ICNC_STATUS_BIT_WAIT_INPUT_ERROR
			    ICNC_STATUS_BIT_EEWRITE_ERROR)
	       Output :
		   ICNCUSB_SUCCESS si communication ok
	       """
	       return self.ICNC2Lib._ICNC_ErrorReset(ErrorBits)

	def GetBoardStatus(self, StatusType): # output param:      *Status 
	       """
	       d'etat interne de la carte par un seul appel a cette fonction.
	       Pour eviter de surcharger la communication, faite une demande approriee en fonction
	       des informations necessaire a l'instant donne.
	       Input :
		     StatusType : combinaison des bits d'etat a lire
			        (exemple : ICNC_STATUS_BOARD_STATUS | ICNC_STATUS_BUFFER_FREE
	       Output :
		    Status : pointeur sur une zone memoire permettant le stockage de tous les
			     etats demandes.
	       Result :  ICNCUSB_SUCCESS si communication ok
		      Exemple1 : Lecture simultanee du status de la carte, de la place disponible dans le buffer
			et de la position actuelle des axes X, Y et Z
		       Status DWORD[5];
	        ICNC_GetBoardStatus( ICNC_STATUS_BOARD_STATUS | ICNC_STATUS_BUFFER_FREE
				    | ICNC_STATUS_ACTUALX | ICNC_STATUS_ACTUALY | ICNC_STATUS_ACTUALZ,
				    &Status);
	       """
	       myInt = ctypes.c_int()
	       self.ICNC2Lib._ICNC_GetBoardStatus(StatusType,ctypes.byref(myInt))
	       return myInt

	def SetOutputAll(self, OutputState):
	       """
	       Forcage de l'etat des sorties
	       Entree :
		   OutputState = bits de sorties a activer
	       """
	       self.notImplemented()
	       return -1

	def SetOverrideValue(self, OverrideValue):
	       """
	       Ecriture de la valeur de survitesse appliquee sur les commandes de deplacement.
	       Input : OverrideValue = Sur vitesse en % de la vitesse de deplacement en cours.
	       """
	       self.notImplemented()
	       return -1

	def GetOverrideValue(self): # output param: *OverrideValue 
	       """
	       Lecture de la valeur actuelle d'override
	       """
	       self.notImplemented()
	       return -1


	def Probe(self, Axe,  Direction,  InNo,  InValue,  MaxStroke,  Speed,  FStart,  Accel,  Decel):
	       """
	       Lancement d'une procedure de palpage sur un axe
	       Entrees :
		     DWORD Axe : axe concerne (AXE_X ou AXE_Y...)
		     DWORD Direction : 0 si negative, 1 si positive
		     DWORD InNo : Numero de l'entree du palpeur
		     BOOL InValue : Valeur attendue sur le palpeur (0 ou 1)
		     DWORD MaxStroke : course maximum de recherche du palpeur
		     DWORD Speed : Vitesse de deplacement vers le capteur
		     DWORD FStart : Frequence de demarrage de l'axe  (Hz)
		     DWORD Accel : Acceleration  (KHz/s)
		     DWORD Decel : Deceleration  (KHz/s)
		      L'utilisation de cette fonction pour le palpage permet de continuer le dialogue avec la carte durant l'operation de palpage.
	       Durant cette operation, il est ainsi possible de lire les status de la carte pour affichage.
	       Le bit de status ICNC_STATUS_BIT_PROBING reste a 1 tant que l'operation n'est pas terminee.
	       Lorsque l'operation est terminee, le bit ICNC_STATUS_BIT_PROBING passe a 0.
	       Il est alors necessaire de tester le bit de status ICNC_STATUS_BIT_PROBING_ERROR pour determiner si l'operation s'est deroulee correctement.
	       Si tel est le cas, la position de l'axe au moment de la detection du contact peut etre lue par l'interrogation de status
	       avec la demande ICNC_STATUS_LAST_PROBE
	       """
	       self.notImplemented()
	       return -1


	def ProbeAndReadBack(self, Axe,  Direction,  InNo,  InValue,  MaxStroke,  Speed,  FStart,  Accel,  Decel): # output param: * ProbePosition 
	       """
	       Lancement d'une procedure de palpage sur un axe et attente du resultat
	       Fonctionnement identique a la fonction ICNC_Probe mais bloquante jusqu'a l'obtention du resultat
	       Entrees :
		     DWORD Axe : axe concerne (AXE_X ou AXE_Y...)
		     DWORD Direction : 0 si positive, 1 si negative
		     DWORD InNo : Numero de l'entree du palpeur
		     BOOL InValue : Valeur attendue sur le palpeur (0 ou 1)
		     DWORD MaxStroke : course maximum de recherche du palpeur
		     DWORD Speed : Vitesse de deplacement vers le capteur
		     DWORD FStart : Frequence de demarrage de l'axe
		     DWORD Accel : Acceleration
		     DWORD Decel : Deceleration
	        Sortie :
		     INT* ProbePosition : Position de l'axe lors de la detection du palpeur
	        Resultat :
		   ICNCUSB_SUCCESS si l'operation s'est deroule correctement
		   ICNCUSB_PROBE_ERROR si erreur de parametre ou palpeur non trouvee dans la course indiquee
		   ICNCUSB_FAIL si erreur de communication
	       """
	       self.notImplemented()
	       return -1

	def SlowStopMotors(self, Axis):
	       """
	       Arret avec rampe des axes indiques
	       """
	       self.notImplemented()
	       return -1

	def SlowStopAllAndClear(self):
	       """
	       Arret avec rampe et vidage buffer
	       """
	       self.notImplemented()
	       return -1

	def StopMotorsAllAndClear(self):
	       """
	       Arret sans rampe et vidage buffer
	       """
	       self.notImplemented()
	       return -1


	def GetOutputAll(self): # output param: *OutputState 
	       """
	       Lecture de l'etat des sorties
	       """
	       self.notImplemented()
	       return -1


	def GetInput(self, InNo): # output param:  *InputState 
	       """
	       Lecture de l'etat d'une des entrees
	       """
	       self.notImplemented()
	       return -1


	def GetInputAll(self): # output param:   *InputState 
	       """
	       Lecture de toutes les entrees
	       """
	       self.notImplemented()
	       return -1


	def GetAnalog(self,    AnalogNo): # output param:  *AnalogValue 
	       """
	       Lecture d'une entree analogique
	       """
	       self.notImplemented()
	       return -1


	def SetOutput(self,    OutputNo, OutputState):
	       """
	       Set de l'etat d'une sortie
	       """
	       self.notImplemented()
	       return -1


	def SetAnalog(self, AnalogNo,  AnalogValue):
	       """
	       Set de l'etat d'une sortie analogique
	       Entrees :
		   AnalogNo : Numero de l'entree analogique : ICNC_ANALOG1 ou ICNC_ANALOG2...
		   AnalogValue :  resolution de l'ADC obtenue par   ICNC_GetSysInfo( ICNC_SYS_INFO_ADC_RESOLUTION)
	       """
	       self.notImplemented()
	       return -1


	def GetExecTime (self): # output param: *ExecTime 
	       """
	       Get total elapsed time in mouvement  (in ms unit)
	       """
	       self.notImplemented()
	       return -1


	def GetSoftwareKeyValue(self): # output param: *SoftwareKeyValue 
	       """
	       Lecture licence logiciel		       
	       """
	       self.notImplemented()
	       return -1


	def LockBoard(self):
	       """
	       Lecture licence logiciel		       
	       """
	       self.notImplemented()
	       return -1


	def GetBufferStatus(self): # output param: *FreeBufferSpace 
	       """
	       Lecture de la place disponible dans le buffer carte
	       """
	       self.notImplemented()
	       return -1

	def Unfreeze(self):
	       """
	       Deverouillage du traitement du buffer
	       forcer le dedblocage du buffer pour executer les commande presentes.
	       A utiliser en conjonction avec la fonction ICNC_FreezeBuf lors de la gestion
	       de la cinematique a l'aide de micro vecteurs
	       """
	       self.notImplemented()
	       return -1


	def WriteUserMem(self, MemoryNumber,  MemoryValue):
	       """
	       Ecriture non bufferisee d'une des cellules memoire utilisateur
	       Memory number = 0 a 9
	       """
	       self.notImplemented()
	       return -1

	def ReadUserMem(self,   MemoryNumber): # output param:   *MemoryValue 
	        """
	        """
	        self.notImplemented()
	        return -1

	def ReadEEPROM(self, StartAdress,  Length): # output param:   BYTE* Value 
	        """
	        """
	        self.notImplemented()
	        return -1

	def WriteEEPROM(self, StartAdress,  Length, WaitCompletion=True,  TimeOut=1000): # output param: BYTE* Value 
	        """
	        """
	        self.notImplemented()
	        return -1

	def ReadParameter(self, ParameterID): # output param: *ParameterValue 
	       """
	       Lecture d'un parametre carte. Voir definition dans GLOBALDEF.H
	       """
	       self.notImplemented()
	       return -1


	def WriteParameter(self, ParameterID,  ParameterValue,  WaitCompletion=True,  TimeOut=1000):
	       """
	       Ecriture d'un parametre carte
	       Par defaut, cette fonction attends et verifie l'ecriture du parametre dans un temps limite de 1000ms
	       """
	       self.notImplemented()
	       return -1

	def WritePosition(self, Axis, PositionX=0, PositionY=0, PositionZ=0, PositionA=0, PositionB=0):
	        """
	        Write internal motor position
	        Ecriture dans les compteurs internes de position
	        """
	        self.notImplemented()
	        return -1


	def MachineHome(self, Axis, MaxStrokeX=0xFFFFFFFF, MaxStrokeY=0xFFFFFFFF, MaxStrokeZ=0xFFFFFFFF, MaxStrokeA=0xFFFFFFFF, MaxStrokeB=0xFFFFFFFF):
	       """
	       Lancement d'une procedure d'origine d'un ou plusieurs axes
	       Entrees :
		   DWORD Axis : Axes concernes (AXE_X | AXE_Y ...)
		      Cette fonction n'est pas bloquante. Il est donc possible de communiquer avec la carte durant la prise d'origine
	       Durant le traitement de cette fonction, le bit de status ICNC_STATUS_BIT_HOMING est a 1
	       Lorsque ce bit passe a 0, interroger le bit de status ICNC_STATUS_BIT_HOMING pour determiner si
	       le traitement s'est deroule correctement.
	       """
	       self.notImplemented()
	       return -1

	def SetTHCTarget(self, THCTargetValue):
	       """
	       Fonction specifique pour machine de decoupe plasma
	       """
	       self.notImplemented()
	       return -1

	def ConfigPrompt(self, PromptState):
	       """
	       Non utilise
	       """
	       self.notImplemented()
	       return -1

	def SetUSBSpeedMode(self, EnableHighSpeed):
	       """
	       """
	       self.notImplemented()
	       return -1

	def GetSysInfo(self, SysInfoType): # output param: *SysInfo 
	       """
	       Lecture des informations systems de la carte.
	       Entrees :
		   DWORD SysInfoType : bits indiquant les informations a lire
				 (voir definition des bits ICNC_SYS_INFO_xxxxxxx)
	       Sortie :
		   DWORD *SysInfo : structure contenant les resultats des informations demandees
	       """
	       self.notImplemented()
	       return -1

	def MoveProfileAbsAsync(self, Axe, FStartStop, Accel, Speed, Decel,   Position):
	       """
	       Lancement d'un mouvement independent sur un axe.
	       Si un mouvement est deja en cours, la nouvelle position cible est mise a jour.
	       Le profile de vitesse est alors recalcule pour s'adapter a la nouvelle cible.
	       Si l'axe est deja en mouvement et la cible inchangee, la commande prend en compte la nouvlle vitesse et le profile est ajuste.
	       """
	       self.notImplemented()
	       return -1

	def MoveProfileRelAsync(self, Axe, FStartStop, Accel, Speed, Decel,   Distance):
	       """
	       Lancement d'un mouvement independent sur un axe.
	       Si un mouvement est deja en cours, la nouvelle position cible est mise a jour.
	       Le profile de vitesse est alors recalcule pour s'adapter a la nouvelle cible.
	       Si l'axe est deja en mouvement et la cible inchangee, la commande prend en compte la nouvlle vitesse et le profile est ajuste.
	       """
	       self.notImplemented()
	       return -1

	def UpdateSpeed(self, Axe,  NewFrenquency):
	       """
	       Modification en dynamique d'un mouvement lance avec la commande de deplacement anynchrone.
	       Si l'axe n'est pas en mouvement, la commande est ignoree.
	       Les modifications de vitesses se font en respectant les rampes d'accel et de decel indiquee par la commande de deplacement
	       La commande prend effet immediatement et n'est donc pas bufferisee.
	       """
	       self.notImplemented()
	       return -1

	def SetTHCStateBuf(self, EnableTHC,   BufferizedCommand):
	       """
	       Activation/desactivation logiciel du THC
	       La commande peut etre bufferisee ou directe
	       Note : Si le logciel doit prendre en charge l'activationdesactivation du THC, mettre
	       le parammetre EE_THC_ACTIVATION_OUTPUT a 0 pour eviter les conflicts
	       """
	       self.notImplemented()
	       return -1

	def FreezeBuf (self):
	       """
	       Freeze buffer treatement until buffer unfreezed or buffer full
	       """
	       self.notImplemented()
	       return -1


	def SetOverrideStateBuf(self, OverrideState):
	       """
	       Enable or disable the override mode
	       """
	       self.notImplemented()
	       return -1

	def SetOutputBuf(self, OutputNo, OutputValue):
	       """
	       """
	       self.notImplemented()
	       return -1

	def SetOutputAllBuf(self, OutputValue):
	       """
	       """
	       self.notImplemented()
	       return -1

	def SetAnalogBuf(self, OutputNo, OutputValue):
	       """
	       """
	       self.notImplemented()
	       return -1

	def WaitBuf(self, TimeToWait):
	       """
	       Temporisation
	       TimeToWait en 100ms
	       """
	       self.notImplemented()
	       return -1


	def WaitInputStateBuf(self, InputNo, InputValue, TimeOut, LockIfError=False, ClearBufferIfError = False):
	       """
	       Attentre l'etat d'une entree
	       L'execution du buffer de commande est gele en attendant l'entree concernee
	       """
	       self.notImplemented()
	       return -1

	def WriteUserMemBuf (self, MemNumber,  Value):
	       """
	       Ecriture non bufferisee d'une des cellules memoire utilisateur
	       Memory number = 0 a 9
	       """
	       self.notImplemented()
	       return -1

	def MoveSpeedRelBuf(self, Speed, MoveX, MoveY, MoveZ, MoveA, MoveB): # output param: *BufferRequired=NULL 
	       """
	       Relative movement without speed profile
	       Use local buffer for full frame transmission
	       Deplacement relatif dans profile (vitesse constante) utilisant un buffer local
	       sur le PC afin d'envoyer des trames completes sur la cartee et optimiser le flux de communication USB
	       """
	       self.notImplemented()
	       return -1

	def MoveSpeedRelLocalBuf(self, Speed, MoveX, MoveY, MoveZ, MoveA, MoveB): # output param: *BufferRequired=NULL 
	       """
	       """
	       self.notImplemented()
	       return -1

	def MoveSpeedAbsBuf(self, Axis, Speed, MoveX, MoveY, MoveZ, MoveA, MoveB): # output param: *BufferRequired=NULL 
	       """
	       Absolute movement without speed profile
	       Deplacement a une position absolue avec profile (trapezoidale) utilisant un buffer local
	       sur le PC afin d'envoyer des trames completes sur la cartee et optimiser le flux de communication USB
	       """
	       self.notImplemented()
	       return -1

	def MoveSpeedAbsLocalBuf(self, Axis, Speed, MoveX, MoveY, MoveZ, MoveA, MoveB): # output param: *BufferRequired=NULL 
	       """
	       Absolute movement without speed profile
	       Use local buffer for full frame transmission
	       !!! Don't forget to use ICNC_FlushLocalBuf at the end
	       Deplacement a une position absolue sans profile (vitesse constante) utilisant un buffer local
	       sur le PC afin d'envoyer des trames completes sur la cartee et optimiser le flux de communication USB
	       """
	       self.notImplemented()
	       return -1

	def FlushLocalBuf(self):
	       """
	       Vidage du buffer local PC et envoie à la carte.
	       """
	       self.notImplemented()
	       return -1

	def MoveProfileRelBuf(self,Speed, MoveX, MoveY, MoveZ, MoveA, MoveB): # output param: *BufferRequired=NUL
	       """
	       Relative movement with speed profile
	       """
	       self.notImplemented()
	       return -1

	def MoveProfileAbsBuf(self, Axis, Speed, PositionX, PositionY, PositionZ, PositionA, PositionB): # output param: *BufferRequired=NULL 
	       """
	       Absolute position movement with speed profile
	       """
	       self.notImplemented()
	       return -1

	def PushPulsesData (self,  nbBytes,  Frequency): # output param: unsigned char *ptBuffer   *BufferRequired=NULL
	       """
	       Envoie d'un tableau de pulses/direction a la carte
	       Codage : Les octets du buffer peuvent etres des affectations de sens de rotation ou des pulses sur les sorties CLK.
				    Octet de direction : 0x40 | DIRECTION   avec DIRECTION = etat des 5 sorties de direction
			     Octet de pas       : 0x20 | PULSES		avec PULSES qui indique sur quels sortie CLK generer des pulses
	       Exemple : [0x41, 0x21, 0x23, 0x21]  aura pour effet d'activer la sortie DIR1 et de generer 3 pas sur CLK1 et 1 pas sur CLK2
	       La frequence de traitement du tableau etant indiquee dans le parametre Frequency
	       """
	       self.notImplemented()
	       return -1

	def ProcessEvent(self, Event, Param):
	        """
	        """
	        self.notImplemented()
	        return -1

	def EventProcessing(self):
	        """
	        Return 0 when process event in completed
	        Return 0xFFFF when process event has been canceled
	        Return Actual event iD during treatement
	        """
	        self.notImplemented()
	        return -1

	def GetCuttingSpeed(self):
	        """
	        if speed defined in ICNC2.DLL, return speed in mm/mn
	        else return 0;
	        """
	        self.notImplemented()
	        return -1

	def SetLanguage(self, Language):
	        """
	        define LANG_ENGLISH     0
	        define LANG_DEUTSCH     1
	        define LANG_FRANCAIS    2
	        define LANG_ITALIANO    3
	        """
	        self.notImplemented()
	        return -1

	def SetVerboseMode(self, Verbose):
	        """
	        """
	        self.notImplemented()
	        return -1

	def SetTorchDownParams(self, ToolNumber, OriginZ, HeadUpZ, ProbeTorchOffsetZ, ProbingMarginZ, FastSpeedDownZ, ProbingSpeedZ, FastSpeedUpZ, ProbeInputNumber, ProbeInputState):
	        """
	        Receive cutting condition from GALAAD
	        """
	        self.notImplemented()
	        return -1

	def PlasmaSettingDlg(self): # output param:  double* HPercage  double* TPercage  double* HCoupe  double* Vitesse  double* THCVoltage  double* Intensite int*  PalpageOne  int*  THCActif  int*  ControlePoste  int*  Simulation 
	        """
	        """
	        self.notImplemented()
	        return -1

	def SwitchToBootLoaderMode(self,   BootKey):
	        """
	        Passage de la carte en mode bootloader pour transfert d'une mise a jour firmware.
	        """
	        self.notImplemented()
	        return -1

	def notImplemented(self):
	        """
	        Que faire si une fonction non implemented est appelee.
	        """
	        sys.exit(-1)
	        return -1

if __name__ == "__main__":
        print("hy")
        i = ICNC2()
        print("connection : ",i.Connect())
        status = i.ICNC_STATUS_BOARD_STATUS | i.ICNC_STATUS_BUFFER_FREE | i.ICNC_STATUS_ACTUALX | i.ICNC_STATUS_ACTUALY | i.ICNC_STATUS_ACTUALZ
        print("board status : ",i.GetBoardStatus(status))
