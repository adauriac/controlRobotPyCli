import ctypes

def GetDLLVersion(void):
	"""
	Retourne le numero de la dll
	"""
	print('non implemente')
	return 0


def SetSimulationMode(   SimulationModeVal):
	"""
	Permet de passer la DLL en mode simulation sans communication physique
	avec la carte. Il est ainsi possible de tester le programme pour ce qui est
	des acces aux fonctions de la DLL
	Input : True pour passer en mode simulation
	"""
	print('non implemente')
	return 0


def Connect( ICNC_Number):
	"""
	Initialisation de la communication avec la carte InterpCNC
	"""
	print('non implemente')
	return 0


def SetUserApplicationID( lUserApplicationID):
	"""
	Definition de l'ID application
	"""
	print('non implemente')
	return 0


def Disconnect( void):
	"""
	Arret de la communication avec la carte InterpCNC
	"""
	print('non implemente')
	return 0


def ErrorReset( ErrorBits):
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
	print('non implemente')
	return 0


def GetBoardStatus( StatusType): # output param:      *Status 
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
	print('non implemente')
	return 0


def SetOutputAll( OutputState):
	"""
	Forcage de l'etat des sorties
	Entree :
	     OutputState = bits de sorties a activer
	"""
	print('non implemente')
	return 0


def SetOverrideValue( OverrideValue):
	"""
	Ecriture de la valeur de survitesse appliquee sur les commandes de deplacement.
	Input : OverrideValue = Sur vitesse en % de la vitesse de deplacement en cours.
	"""
	print('non implemente')
	return 0


def GetOverrideValue(): # output param: *OverrideValue 
	"""
	Lecture de la valeur actuelle d'override
	"""
	print('non implemente')
	return 0


def Probe( Axe,  Direction,  InNo,  InValue,  MaxStroke,  Speed,  FStart,  Accel,  Decel):
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
	print('non implemente')
	return 0


def ProbeAndReadBack( Axe,  Direction,  InNo,  InValue,  MaxStroke,  Speed,  FStart,  Accel,  Decel): # output param: * ProbePosition 
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
	print('non implemente')
	return 0


def SlowStopMotors( Axis):
	"""
	Arret avec rampe des axes indiques
	"""
	print('non implemente')
	return 0


def SlowStopAllAndClear(void):
	"""
	Arret avec rampe et vidage buffer
	"""
	print('non implemente')
	return 0


def StopMotorsAllAndClear(void):
	"""
	Arret sans rampe et vidage buffer
	"""
	print('non implemente')
	return 0


def GetOutputAll(): # output param: *OutputState 
	"""
	Lecture de l'etat des sorties
	"""
	print('non implemente')
	return 0


def GetInput( InNo): # output param:  *InputState 
	"""
	Lecture de l'etat d'une des entrees
	"""
	print('non implemente')
	return 0


def GetInputAll(): # output param:   *InputState 
	"""
	Lecture de toutes les entrees
	"""
	print('non implemente')
	return 0


def GetAnalog(    AnalogNo): # output param:  *AnalogValue 
	"""
	Lecture d'une entree analogique
	"""
	print('non implemente')
	return 0


def SetOutput(    OutputNo, OutputState):
	"""
	Set de l'etat d'une sortie
	"""
	print('non implemente')
	return 0


def SetAnalog( AnalogNo,  AnalogValue):
	"""
	Set de l'etat d'une sortie analogique
	Entrees :
	     AnalogNo : Numero de l'entree analogique : ICNC_ANALOG1 ou ICNC_ANALOG2...
	     AnalogValue :  resolution de l'ADC obtenue par   ICNC_GetSysInfo( ICNC_SYS_INFO_ADC_RESOLUTION)
	"""
	print('non implemente')
	return 0


def GetExecTime (): # output param: *ExecTime 
	"""
	Get total elapsed time in mouvement  (in ms unit)
	"""
	print('non implemente')
	return 0


def GetSoftwareKeyValue(): # output param: *SoftwareKeyValue 
	"""
	Lecture licence logiciel                         
	"""
	print('non implemente')
	return 0


def LockBoard(void):
	"""
	Lecture licence logiciel                         
	"""
	print('non implemente')
	return 0


def GetBufferStatus(): # output param: *FreeBufferSpace 
	"""
	Lecture de la place disponible dans le buffer carte
	"""
	print('non implemente')
	return 0


def Unfreeze(void):
	"""
	Deverouillage du traitement du buffer
	forcer le dedblocage du buffer pour executer les commande presentes.
	A utiliser en conjonction avec la fonction ICNC_FreezeBuf lors de la gestion
	de la cinematique a l'aide de micro vecteurs
	"""
	print('non implemente')
	return 0


def WriteUserMem( MemoryNumber,  MemoryValue):
	"""
	Ecriture non bufferisee d'une des cellules memoire utilisateur
	Memory number = 0 a 9
	"""
	print('non implemente')
	return 0


def ReadUserMem(   MemoryNumber): # output param:   *MemoryValue 
	"""
	"""
	print('non implemente')
	return 0


def ReadEEPROM( StartAdress,  Length): # output param:   BYTE* Value 
	"""
	"""
	print('non implemente')
	return 0


def WriteEEPROM( StartAdress,  Length, WaitCompletion=True,  TimeOut=1000): # output param: BYTE* Value 
	"""
	"""
	print('non implemente')
	return 0


def ReadParameter( ParameterID): # output param: *ParameterValue 
	"""
	Lecture d'un parametre carte. Voir definition dans GLOBALDEF.H
	"""
	print('non implemente')
	return 0


def WriteParameter( ParameterID,  ParameterValue,  WaitCompletion=True,  TimeOut=1000):
	"""
	Ecriture d'un parametre carte
	Par defaut, cette fonction attends et verifie l'ecriture du parametre dans un temps limite de 1000ms
	"""
	print('non implemente')
	return 0


def WritePosition( Axis, PositionX=0, PositionY=0, PositionZ=0, PositionA=0, PositionB=0):
	"""
	Write internal motor position
	Ecriture dans les compteurs internes de position
	"""
	print('non implemente')
	return 0


def MachineHome( Axis, MaxStrokeX=0xFFFFFFFF, MaxStrokeY=0xFFFFFFFF, MaxStrokeZ=0xFFFFFFFF, MaxStrokeA=0xFFFFFFFF, MaxStrokeB=0xFFFFFFFF):
	"""
	Lancement d'une procedure d'origine d'un ou plusieurs axes
	Entrees :
	     DWORD Axis : Axes concernes (AXE_X | AXE_Y ...)
		Cette fonction n'est pas bloquante. Il est donc possible de communiquer avec la carte durant la prise d'origine
	Durant le traitement de cette fonction, le bit de status ICNC_STATUS_BIT_HOMING est a 1
	Lorsque ce bit passe a 0, interroger le bit de status ICNC_STATUS_BIT_HOMING pour determiner si
	le traitement s'est deroule correctement.
	"""
	print('non implemente')
	return 0


def SetTHCTarget( THCTargetValue):
	"""
	Fonction specifique pour machine de decoupe plasma
	"""
	print('non implemente')
	return 0


def ConfigPrompt( PromptState):
	"""
	Non utilise
	"""
	print('non implemente')
	return 0


def SetUSBSpeedMode( EnableHighSpeed):
	"""
	"""
	print('non implemente')
	return 0


def GetSysInfo( SysInfoType): # output param: *SysInfo 
	"""
	Lecture des informations systems de la carte.
	Entrees :
	     DWORD SysInfoType : bits indiquant les informations a lire
	                     (voir definition des bits ICNC_SYS_INFO_xxxxxxx)
	Sortie :
	     DWORD *SysInfo : structure contenant les resultats des informations demandees
	"""
	print('non implemente')
	return 0


def MoveProfileAbsAsync( Axe, FStartStop, Accel, Speed, Decel,   Position):
	"""
	Lancement d'un mouvement independent sur un axe.
	Si un mouvement est deja en cours, la nouvelle position cible est mise a jour.
	Le profile de vitesse est alors recalcule pour s'adapter a la nouvelle cible.
	Si l'axe est deja en mouvement et la cible inchangee, la commande prend en compte la nouvlle vitesse et le profile est ajuste.
	"""
	print('non implemente')
	return 0


def MoveProfileRelAsync( Axe, FStartStop, Accel, Speed, Decel,   Distance):
	"""
	Lancement d'un mouvement independent sur un axe.
	Si un mouvement est deja en cours, la nouvelle position cible est mise a jour.
	Le profile de vitesse est alors recalcule pour s'adapter a la nouvelle cible.
	Si l'axe est deja en mouvement et la cible inchangee, la commande prend en compte la nouvlle vitesse et le profile est ajuste.
	"""
	print('non implemente')
	return 0


def UpdateSpeed( Axe,  NewFrenquency):
	"""
	Modification en dynamique d'un mouvement lance avec la commande de deplacement anynchrone.
	Si l'axe n'est pas en mouvement, la commande est ignoree.
	Les modifications de vitesses se font en respectant les rampes d'accel et de decel indiquee par la commande de deplacement
	La commande prend effet immediatement et n'est donc pas bufferisee.
	"""
	print('non implemente')
	return 0


def SetTHCStateBuf( EnableTHC,   BufferizedCommand):
	"""
	Activation/desactivation logiciel du THC
	La commande peut etre bufferisee ou directe
	Note : Si le logciel doit prendre en charge l'activationdesactivation du THC, mettre
	le parammetre EE_THC_ACTIVATION_OUTPUT a 0 pour eviter les conflicts
	"""
	print('non implemente')
	return 0


def FreezeBuf (void):
	"""
	Freeze buffer treatement until buffer unfreezed or buffer full
	"""
	print('non implemente')
	return 0


def SetOverrideStateBuf( OverrideState):
	"""
	Enable or disable the override mode
	"""
	print('non implemente')
	return 0


def SetOutputBuf( OutputNo, OutputValue):
	"""
	"""
	print('non implemente')
	return 0


def SetOutputAllBuf( OutputValue):
	"""
	"""
	print('non implemente')
	return 0


def SetAnalogBuf( OutputNo, OutputValue):
	"""
	"""
	print('non implemente')
	return 0


def WaitBuf( TimeToWait):
	"""
	Temporisation
	TimeToWait en 100ms
	"""
	print('non implemente')
	return 0


def WaitInputStateBuf( InputNo, InputValue, TimeOut, LockIfError=False, ClearBufferIfError = False):
	"""
	Attentre l'etat d'une entree
	L'execution du buffer de commande est gele en attendant l'entree concernee
	"""
	print('non implemente')
	return 0


def WriteUserMemBuf ( MemNumber,  Value):
	"""
	Ecriture non bufferisee d'une des cellules memoire utilisateur
	Memory number = 0 a 9
	"""
	print('non implemente')
	return 0


def MoveSpeedRelBuf( Speed, MoveX, MoveY, MoveZ, MoveA, MoveB): # output param: *BufferRequired=NULL 
	"""
	Relative movement without speed profile
	Use local buffer for full frame transmission
	Deplacement relatif dans profile (vitesse constante) utilisant un buffer local
	sur le PC afin d'envoyer des trames completes sur la cartee et optimiser le flux de communication USB
	"""
	print('non implemente')
	return 0


def MoveSpeedRelLocalBuf( Speed, MoveX, MoveY, MoveZ, MoveA, MoveB): # output param: *BufferRequired=NULL 
	"""
	"""
	print('non implemente')
	return 0


def MoveSpeedAbsBuf( Axis, Speed, MoveX, MoveY, MoveZ, MoveA, MoveB): # output param: *BufferRequired=NULL 
	"""
	Absolute movement without speed profile
	Deplacement a une position absolue avec profile (trapezoidale) utilisant un buffer local
	sur le PC afin d'envoyer des trames completes sur la cartee et optimiser le flux de communication USB
	"""
	print('non implemente')
	return 0


def MoveSpeedAbsLocalBuf( Axis, Speed, MoveX, MoveY, MoveZ, MoveA, MoveB): # output param: *BufferRequired=NULL 
	"""
	Absolute movement without speed profile
	Use local buffer for full frame transmission
	!!! Don't forget to use ICNC_FlushLocalBuf at the end
	Deplacement a une position absolue sans profile (vitesse constante) utilisant un buffer local
	sur le PC afin d'envoyer des trames completes sur la cartee et optimiser le flux de communication USB
	"""
	print('non implemente')
	return 0


def FlushLocalBuf(void):
	"""
	Vidage du buffer local PC et envoie a la carte.
	"""
	print('non implemente')
	return 0


def MoveProfileRelBuf( Speed, MoveX, MoveY, MoveZ, MoveA, MoveB): # output param: *BufferRequired=NULL 
	"""
	Relative movement with speed profile
	"""
	print('non implemente')
	return 0


def MoveProfileAbsBuf( Axis, Speed, PositionX, PositionY, PositionZ, PositionA, PositionB): # output param: *BufferRequired=NULL 
	"""
	Absolute position movement with speed profile
	"""
	print('non implemente')
	return 0


def PushPulsesData (  nbBytes,  Frequency): # output param: unsigned char *ptBuffer   *BufferRequired=NULL 
	"""
	Envoie d'un tableau de pulses/direction a la carte
	Codage : Les octets du buffer peuvent etres des affectations de sens de rotation ou des pulses sur les sorties CLK.
				Octet de direction : 0x40 | DIRECTION   avec DIRECTION = etat des 5 sorties de direction
			Octet de pas       : 0x20 | PULSES		avec PULSES qui indique sur quels sortie CLK generer des pulses
	Exemple : [0x41, 0x21, 0x23, 0x21]  aura pour effet d'activer la sortie DIR1 et de generer 3 pas sur CLK1 et 1 pas sur CLK2
	La frequence de traitement du tableau etant indiquee dans le parametre Frequency
	"""
	print('non implemente')
	return 0


	"""
	**********************************  Fonctions specifiques GALAAD							      
	define	EVENT_MANUALCONTROL  0
	define	EVENT_STARTPROCESS   1
	define	EVENT_RAPIDTOXY      2
	define	EVENT_TOOLDOWN       3
	define	EVENT_DRILLING       4
	define	EVENT_FEEDING        5
	define	EVENT_LIFTUP         6
	define	EVENT_PARKTOOL       7
	define	EVENT_ENDPROCESS     8
	define       EVENT_BREAKPROCESS   0xFFFF
	"""
	print('non implemente')
	return 0


def ProcessEvent( Event, Param):
	"""
	"""
	print('non implemente')
	return 0


def EventProcessing(void):
	"""
	Return 0 when process event in completed
	Return 0xFFFF when process event has been canceled
	Return Actual event iD during treatement
	"""
	print('non implemente')
	return 0


def GetCuttingSpeed(void):
	"""
	if speed defined in ICNC2.DLL, return speed in mm/mn
	else return 0;
	"""
	print('non implemente')
	return 0


def SetLanguage( Language):
	"""
	define LANG_ENGLISH     0
	define LANG_DEUTSCH     1
	define LANG_FRANCAIS    2
	define LANG_ITALIANO    3
	"""
	print('non implemente')
	return 0


def SetVerboseMode( Verbose):
	"""
	"""
	print('non implemente')
	return 0


def SetTorchDownParams( ToolNumber, OriginZ, HeadUpZ, ProbeTorchOffsetZ, ProbingMarginZ, FastSpeedDownZ, ProbingSpeedZ, FastSpeedUpZ, ProbeInputNumber, ProbeInputState):
	"""
	Receive cutting condition from GALAAD
	"""
	print('non implemente')
	return 0


def PlasmaSettingDlg(): # output param:  double* HPercage  double* TPercage  double* HCoupe  double* Vitesse  double* THCVoltage  double* Intensite int*  PalpageOne  int*  THCActif  int*  ControlePoste  int*  Simulation 
	"""
	"""
	print('non implemente')
	return 0


def SwitchToBootLoaderMode(   BootKey):
	"""
	Passage de la carte en mode bootloader pour transfert d'une mise a jour firmware.
	"""
	print('non implemente')
	return 0


