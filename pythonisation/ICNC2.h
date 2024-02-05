/*********************************************************************
 *
 *                  InterpCNC USB Library
 *
 *********************************************************************
 * FileName:        ICNC_USBAPI.h
 * Dependencies:    None
 * Compiler:        C++
 * Company:         Copyright (C) 2009 by SOPROLEC
 * Date
 *
 *********************************************************************/

#ifndef _ICNC_USBAPI_
#define _ICNC_USBAPI_

#include <Windows.h>

// Valeurs de retour des fonctions de la DLL
#define	ICNCUSB_FAIL                  0
#define ICNCUSB_SUCCESS               1
#define ICNCUSB_COM_ERROR             3
#define ICNCUSB_TIMEOUT               4
#define ICNCUSB_PROBE_ERROR           5


#ifndef _MSC_VER
typedef DWORD (*CONSOLE_HANDLER)(const char *buf);
#else
#endif

EXTERN_C_START

DWORD _ICNC_GetDLLVersion(void);




// Permet de passer la DLL en mode simulation sans communication physique
// avec la carte. Il est ainsi possible de tester le programme pour ce qui est
// des acc�s aux fonctions de la DLL
// Input : TRUE pour passer en mode simulation
//
DWORD _ICNC_SetSimulationMode( BOOL  SimulationModeVal);

// Initialisation de la communication avec la carte InterpCNC
DWORD _ICNC_Connect( DWORD ICNC_Number);


// Definition de l'ID application
DWORD _ICNC_SetUserApplicationID( DWORD lUserApplicationID);

// Arr�t de la communication avec la carte InterpCNC
DWORD _ICNC_Disconnect( void);

// D�v�rouillage carte
// Acquittemement Arr�t d'urgence, Fin de course
// Input : Bits de d�fauts � remettre � 0
//                ICNC_STATUS_BIT_EMERGENCYSTOP
//                ICNC_STATUS_BIT_LOCKED
//                ICNC_STATUS_BIT_HOMING_ERROR
//                ICNC_STATUS_BIT_PROBING_ERROR
//                ICNC_STATUS_BIT_WAIT_INPUT_ERROR
//                ICNC_STATUS_BIT_EEWRITE_ERROR)
// Output :
//      ICNCUSB_SUCCESS si communication ok
DWORD _ICNC_ErrorReset( DWORD ErrorBits);


// Commande NON bufferis�es
// ********************

// Lecture du status de la carte. Il est possible de lire toutes les informations
// d'�tat interne de la carte par un seul appel � cette fonction.
// Pour �viter de surcharger la communication, faite une demande approri�e en fonction
// des informations n�c�ssaire � l'instant donn�.
// Input :
//        StatusType : combinaison des bits d'�tat � lire
//                    (exemple : ICNC_STATUS_BOARD_STATUS | ICNC_STATUS_BUFFER_FREE
// Output :
//       Status : pointeur sur une zone m�moire permettant le stockage de tous les
//                 �tats demand�s.
// Result :  ICNCUSB_SUCCESS si communication ok
//
// Exemple1 : Lecture simultan�e du status de la carte, de la place disponible dans le buffer
//            et de la position actuelle des axes X, Y et Z
//
//  Status DWORD[5];
//  ICNC_GetBoardStatus( ICNC_STATUS_BOARD_STATUS | ICNC_STATUS_BUFFER_FREE
//                         | ICNC_STATUS_ACTUALX | ICNC_STATUS_ACTUALY | ICNC_STATUS_ACTUALZ,
//                         &Status);
DWORD _ICNC_GetBoardStatus(DWORD StatusType,         // Input
                             DWORD *Status);           // Output

// Forcage de l'�tat des sorties
// Entr�e :
//      OutputState = bits de sorties � activer
DWORD _ICNC_SetOutputAll(DWORD OutputState);

// Ecriture de la valeur de survitesse appliqu�e sur les commandes de d�placement.
// Input : OverrideValue = Sur vitesse en % de la vitesse de d�placement en cours.
DWORD _ICNC_SetOverrideValue(DWORD OverrideValue); // Input

// Lecture de la valeur actuelle d'override
DWORD _ICNC_GetOverrideValue(DWORD *OverrideValue); // Outpur

// Lancement d'une proc�dure de palpage sur un axe
// Entr�es :
//        DWORD Axe : axe concern� (AXE_X ou AXE_Y...)
//        DWORD Direction : 0 si n�gative, 1 si positive
//        DWORD InNo : N� de l'entr�e du palpeur
//        BOOL InValue : Valeur attendue sur le palpeur (0 ou 1)
//        DWORD MaxStroke : course maximum de recherche du palpeur
//        DWORD Speed : Vitesse de d�placement vers le capteur
//        DWORD FStart : Fr�quence de d�marrage de l'axe  (Hz)
//        DWORD Accel : Acc�l�ration  (KHz/s)
//        DWORD Decel : D�c�leration  (KHz/s)
//
// L'utilisation de cette fonction pour le palpage permet de continuer le dialogue avec la carte durant l'op�ration de palpage.
// Durant cette op�ration, il est ainsi possible de lire les status de la carte pour affichage.
// Le bit de status ICNC_STATUS_BIT_PROBING reste � 1 tant que l'op�ration n'est pas termin�e.
// Lorsque l'op�ration est termin�e, le bit ICNC_STATUS_BIT_PROBING passe � 0.
// Il est alors n�c�ssaire de tester le bit de status ICNC_STATUS_BIT_PROBING_ERROR pour d�terminer si l'op�ration s'est d�roul�e correctement.
// Si tel est le cas, la position de l'axe au moment de la detection du contact peut �tre lue par l'interrogation de status
// avec la demande ICNC_STATUS_LAST_PROBE
DWORD _ICNC_Probe(DWORD Axe, DWORD Direction, DWORD InNo, BOOL InValue, DWORD MaxStroke, DWORD Speed, DWORD FStart, DWORD Accel, DWORD Decel);

// Lancement d'une proc�dure de palpage sur un axe et attente du r�sultat
// Fonctionnement identique � la fonction ICNC_Probe mais bloquante jusqu'� l'obtention du r�sultat
// Entr�es :
//        DWORD Axe : axe concern� (AXE_X ou AXE_Y...)
//        DWORD Direction : 0 si positive, 1 si n�gative
//        DWORD InNo : N� de l'entr�e du palpeur
//        BOOL InValue : Valeur attendue sur le palpeur (0 ou 1)
//        DWORD MaxStroke : course maximum de recherche du palpeur
//        DWORD Speed : Vitesse de d�placement vers le capteur
//        DWORD FStart : Fr�quence de d�marrage de l'axe
//        DWORD Accel : Acc�l�ration
//        DWORD Decel : D�c�leration
//  Sortie :
//        INT* ProbePosition : Position de l'axe lors de la d�tection du palpeur
//  Resultat :
//      ICNCUSB_SUCCESS si l'op�ration s'est d�roul� correctement
//      ICNCUSB_PROBE_ERROR si erreur de param�tre ou palpeur non trouv�e dans la course indiqu�e
//      ICNCUSB_FAIL si erreur de communication
DWORD _ICNC_ProbeAndReadBack(DWORD Axe, DWORD Direction, DWORD InNo, BOOL InValue, DWORD MaxStroke, DWORD Speed, DWORD FStart, DWORD Accel, DWORD Decel, INT* ProbePosition);

// Arr�t avec rampe des axes indiqu�s
DWORD _ICNC_SlowStopMotors(DWORD Axis);

// Arr�t avec rampe et vidage buffer
DWORD _ICNC_SlowStopAllAndClear(void);

// Arr�t sans rampe et vidage buffer
DWORD _ICNC_StopMotorsAllAndClear(void);

// Lecture de l'�tat des sorties
DWORD _ICNC_GetOutputAll(DWORD *OutputState); // Output

// Lecture de l'�tat d'une des entr�es
DWORD _ICNC_GetInput( DWORD InNo, // Input
                        BOOL *InputState);

// Lecture de toutes les entr�es
DWORD _ICNC_GetInputAll(  DWORD *InputState); // Output

// Lecture d'une entr�e analogique
DWORD _ICNC_GetAnalog(   DWORD AnalogNo, // Input
                           DWORD *AnalogValue);

// Set de l'�tat d'une sortie
DWORD _ICNC_SetOutput(   DWORD OutputNo,
                            BOOL OutputState);

// Set de l'�tat d'une sortie analogique
// Entr�es :
//      AnalogNo : Num�ro de l'entr�e analogique : ICNC_ANALOG1 ou ICNC_ANALOG2...
//      AnalogValue :  r�solution de l'ADC obtenue par   ICNC_GetSysInfo( ICNC_SYS_INFO_ADC_RESOLUTION )
DWORD _ICNC_SetAnalog( DWORD AnalogNo,
                         DWORD AnalogValue);


// Get total elapsed time in mouvement  (in ms unit)
DWORD _ICNC_GetExecTime (  DWORD *ExecTime);



// Lecture licence logiciel                         
DWORD _ICNC_GetSoftwareKeyValue(DWORD *SoftwareKeyValue);

// Lecture licence logiciel                         
DWORD _ICNC_LockBoard(void);




// Lecture de la place disponible dans le buffer carte
DWORD _ICNC_GetBufferStatus(   DWORD *FreeBufferSpace); // Output

// D�v�rouillage du traitement du buffer
// forcer le d�dblocage du buffer pour ex�cuter les commande pr�sentes.
// A utiliser en conjonction avec la fonction ICNC_FreezeBuf lors de la gestion
// de la cin�matique � l'aide de micro vecteurs
//
DWORD _ICNC_Unfreeze(void);

// Ecriture non bufferis�e d'une des cellules m�moire utilisateur
// Memory number = 0 � 9
DWORD _ICNC_WriteUserMem( DWORD MemoryNumber,
                            DWORD MemoryValue);

DWORD _ICNC_ReadUserMem(  DWORD MemoryNumber,
                            DWORD *MemoryValue);

DWORD _ICNC_ReadEEPROM( DWORD StartAdress,
                          DWORD Length,
                          BYTE* Value);


DWORD _ICNC_WriteEEPROM( DWORD StartAdress,
                           DWORD Length,
                           BYTE* Value,
						   #ifndef _MSC_VER
                           BOOL WaitCompletion=TRUE,
                           DWORD TimeOut=1000
						   #else
                           BOOL WaitCompletion,
                           DWORD TimeOut
						   #endif

						   );

// Lecture d'un param�tre carte. Voir d�finition dans GLOBALDEF.H
DWORD _ICNC_ReadParameter( DWORD ParameterID,
                             INT *ParameterValue);

// Ecriture d'un param�tre carte
// Par d�faut, cette fonction attends et v�rifie l'�criture du param�tre dans un temps limit� de 1000ms
DWORD _ICNC_WriteParameter( DWORD ParameterID,
                              DWORD ParameterValue,
							#ifndef _MSC_VER
                              BOOL WaitCompletion=TRUE,
                              DWORD TimeOut=1000
						    #else
                              BOOL WaitCompletion,
                            DWORD TimeOut
						    #endif
							);


// Write internal motor position
// Ecriture dans les compteurs internes de position
DWORD _ICNC_WritePosition( DWORD Axis,
							#ifndef _MSC_VER
                             INT PositionX=0,
                             INT PositionY=0,
                             INT PositionZ=0,
                             INT PositionA=0,
                             INT PositionB=0
							#else
                             INT PositionX,
                             INT PositionY,
                             INT PositionZ,
                             INT PositionA,
                             INT PositionB
 						    #endif

);


// Lancement d'une proc�dure d'origine d'un ou plusieurs axes
// Entr�es :
//      DWORD Axis : Axes concern�s (AXE_X | AXE_Y ...)
//
// Cette fonction n'est pas bloquante. Il est donc possible de communiquer avec la carte durant la prise d'origine
// Durant le traitement de cette fonction, le bit de status ICNC_STATUS_BIT_HOMING est � 1
// Lorsque ce bit passe � 0, interroger le bit de status ICNC_STATUS_BIT_HOMING pour d�terminer si
// le traitement s'est d�roul� correctement.
DWORD _ICNC_MachineHome(   DWORD Axis,
						  	 #ifndef _MSC_VER
                                DWORD MaxStrokeX=0xFFFFFFFF,
                                DWORD MaxStrokeY=0xFFFFFFFF,
                                DWORD MaxStrokeZ=0xFFFFFFFF,
                                DWORD MaxStrokeA=0xFFFFFFFF,
                                DWORD MaxStrokeB=0xFFFFFFFF
							#else
                                DWORD MaxStrokeX,
                                DWORD MaxStrokeY,
                                DWORD MaxStrokeZ,
                                DWORD MaxStrokeA,
                                DWORD MaxStrokeB
 						    #endif
							);



// Fonction sp�cifique pour machine de d�coupe plasma
DWORD _ICNC_SetTHCTarget( DWORD THCTargetValue);

// Non utilis�
DWORD _ICNC_ConfigPrompt( BOOL PromptState);

DWORD _ICNC_SetUSBSpeedMode( BOOL EnableHighSpeed);

// Lecture des informations systems de la carte.
// Entr�es :
//      DWORD SysInfoType : bits indiquant les informations � lire
//                      (voir d�finition des bits ICNC_SYS_INFO_xxxxxxx)
// Sortie :
//      DWORD *SysInfo : structure contenant les r�sultats des informations demand�es
DWORD _ICNC_GetSysInfo( DWORD SysInfoType,
                          DWORD *SysInfo);



// Lancement d'un mouvement ind�pendent sur un axe.
// Si un mouvement est d�j� en cours, la nouvelle position cible est mise � jour.
// Le profile de vitesse est alors recalcul� pour s'adapter � la nouvelle cible.
// Si l'axe est d�j� en mouvement et la cible inchang�e, la commande prend en compte la nouvlle vitesse et le profile est ajust�.

DWORD _ICNC_MoveProfileAbsAsync( DWORD Axe,
                                   DWORD FStartStop,
                                   DWORD Accel,
                                   DWORD Speed,
                                   DWORD Decel,
                                   INT   Position);

DWORD _ICNC_MoveProfileRelAsync( DWORD Axe,
                                   DWORD FStartStop,
                                   DWORD Accel,
                                   DWORD Speed,
                                   DWORD Decel,
                                   INT   Distance);


// Modification en dynamique d'un mouvement lanc� avec la commande de d�placement anynchrone.
// Si l'axe n'est pas en mouvement, la commande est ignor�e.
// Les modifications de vitesses se font en respectant les rampes d'accel et de decel indiqu�e par la commande de d�placement
// La commande prend effet imm�diatement et n'est donc pas bufferis�e.
DWORD _ICNC_UpdateSpeed( DWORD Axe,
                                   DWORD NewFrenquency);


								   
// Fonction non impl�ment�e
DWORD _ICNC_RampUpAbsBuf( DWORD Axis,
                         INT Position[5],
                         DWORD FStart[5],
                         DWORD FEnd[5],
                         DWORD Accel[5]); // Hz/s

// Fonction non impl�ment�e
DWORD _ICNC_RampDownAbsBuf( DWORD Axis,
                         INT Position[5],
                         DWORD FStart[5],
                         DWORD FEnd[5],
                         DWORD Decel[5]);  // Hz/s


// Activation/desactivation logiciel du THC
// La commande peut �tre bufferis�e ou directe
// Note : Si le logciel doit prendre en charge l'activationd�sactivation du THC, mettre
// le paramm�tre EE_THC_ACTIVATION_OUTPUT � 0 pour �viter les conflicts
DWORD _ICNC_SetTHCStateBuf(BOOL EnableTHC,
                          BOOL BufferizedCommand);




// Commande bufferis�es
// ********************

// Freeze buffer treatement until buffer unfreezed or buffer full
DWORD _ICNC_FreezeBuf (void);

// Enable or disable the override mode
DWORD _ICNC_SetOverrideStateBuf(BOOL OverrideState); // Input

DWORD _ICNC_SetOutputBuf( DWORD OutputNo,
                            BOOL OutputValue);
DWORD _ICNC_SetOutputAllBuf( DWORD OutputValue);
DWORD _ICNC_SetAnalogBuf( DWORD OutputNo,
                            DWORD OutputValue);
// Temporisation
// TimeToWait en 100ms
DWORD _ICNC_WaitBuf(DWORD TimeToWait);

// Attentre l'�tat d'une entr�e
// L'ex�cution du buffer de commande est gel� en attendant l'entr�e concern�e
DWORD _ICNC_WaitInputStateBuf(DWORD InputNo,
                                BOOL InputValue,
                                DWORD TimeOut,
                                #ifndef _MSC_VER
								BOOL LockIfError=FALSE,
                                BOOL ClearBufferIfError = FALSE
								#else
								BOOL LockIfError,
                                BOOL ClearBufferIfError
								#endif
								);


// Ecriture non bufferis�e d'une des cellules m�moire utilisateur
// Memory number = 0 � 9
DWORD _ICNC_WriteUserMemBuf (DWORD MemNumber,
                               DWORD Value);

// Relative movement without speed profile
DWORD _ICNC_MoveSpeedRelBuf(DWORD Speed,
                           INT MoveX,
                           INT MoveY,
                           INT MoveZ,
                           INT MoveA,
                           INT MoveB,
						  	#ifndef _MSC_VER
                           DWORD *BufferRequired=NULL
							#else
                           DWORD *BufferRequired
 						    #endif
						   );

// Relative movement without speed profile
// Use local buffer for full frame transmission
// D�placement relatif dans profile (vitesse constante) utilisant un buffer local
// sur le PC afin d'envoyer des trames compl�tes sur la cartee et optimiser le flux de communication USB
DWORD _ICNC_MoveSpeedRelLocalBuf(DWORD Speed,
                               INT MoveX,
                               INT MoveY,
                               INT MoveZ,
                               INT MoveA,
                               INT MoveB,
						  	#ifndef _MSC_VER
							   DWORD *BufferRequired=NULL
							#else
							   DWORD *BufferRequired
 						    #endif
							);

                               



// Absolute movement without speed profile
// D�placement � une position absolue avec profile (trap�zo�dale) utilisant un buffer local
// sur le PC afin d'envoyer des trames compl�tes sur la cartee et optimiser le flux de communication USB

DWORD _ICNC_MoveSpeedAbsBuf( DWORD Axis,
                               DWORD Speed,
                               INT MoveX,
                               INT MoveY,
                               INT MoveZ,
                               INT MoveA,
                               INT MoveB,

						  	#ifndef _MSC_VER
                               DWORD *BufferRequired=NULL
							#else
                               DWORD *BufferRequired
 						    #endif
							);


// Absolute movement without speed profile
// Use local buffer for full frame transmission
// !!! Don't forget to use ICNC_FlushLocalBuf at the end
// D�placement � une position absolue sans profile (vitesse constante) utilisant un buffer local
// sur le PC afin d'envoyer des trames compl�tes sur la cartee et optimiser le flux de communication USB
DWORD _ICNC_MoveSpeedAbsLocalBuf(DWORD Axis,
                                   DWORD Speed,
                                   INT MoveX,
                                   INT MoveY,
                                   INT MoveZ,
                                   INT MoveA,
                                   INT MoveB,
							#ifndef _MSC_VER
                                   DWORD *BufferRequired=NULL
							#else
                                   DWORD *BufferRequired
 						    #endif
							);

// Vidage du buffer local PC et envoie � la carte.
DWORD _ICNC_FlushLocalBuf(void);


// Relative movement with speed profile
DWORD _ICNC_MoveProfileRelBuf(DWORD Speed,
                                INT MoveX,
                                INT MoveY,
                                INT MoveZ,
                                INT MoveA,
                                INT MoveB,
							#ifndef _MSC_VER
                                DWORD *BufferRequired=NULL
							#else
                                DWORD *BufferRequired
 						    #endif
							);


// Absolute position movement with speed profile
DWORD _ICNC_MoveProfileAbsBuf(DWORD Axis,
                                DWORD Speed,
                                INT PositionX,
                                INT PositionY,
                                INT PositionZ,
                                INT PositionA,
                                INT PositionB,

							#ifndef _MSC_VER
                                DWORD *BufferRequired=NULL
							#else
                                DWORD *BufferRequired
 						    #endif
							);

							
							
// Envoie d'un tableau de pulses/direction � la carte
// Codage : Les octets du buffer peuvent �tres des affectations de sens de rotation ou des pulses sur les sorties CLK.
// 			Octet de direction : 0x40 | DIRECTION   avec DIRECTION = �tat des 5 sorties de direction
//			Octet de pas       : 0x20 | PULSES		avec PULSES qui indique sur quels sortie CLK g�n�rer des pulses
// Exemple : [0x41, 0x21, 0x23, 0x21]  aura pour effet d'activer la sortie DIR1 et de g�n�rer 3 pas sur CLK1 et 1 pas sur CLK2
// La fr�quence de traitement du tableau �tant indiqu�e dans le param�tre Frequency

DWORD _ICNC_PushPulsesData ( unsigned char *ptBuffer, 
										 int nbBytes, 
										 DWORD Frequency, 
										 #ifndef _MSC_VER
											DWORD *BufferRequired=NULL
										#else
											DWORD *BufferRequired
										#endif
										);

							
// **********************************  Fonctions sp�cifiques GALAAD								 


//#define	EVENT_MANUALCONTROL  0
//#define	EVENT_STARTPROCESS   1
//#define	EVENT_RAPIDTOXY      2
//#define	EVENT_TOOLDOWN       3
//#define	EVENT_DRILLING       4
//#define	EVENT_FEEDING        5
//#define	EVENT_LIFTUP         6
//#define	EVENT_PARKTOOL       7
//#define	EVENT_ENDPROCESS     8
//#define       EVENT_BREAKPROCESS   0xFFFF
DWORD _ICNC_ProcessEvent(DWORD Event,
                           DWORD Param);


// Return 0 when process event in completed
// Return 0xFFFF when process event has been canceled
// Return Actual event iD during treatement
DWORD _ICNC_EventProcessing(void);

// if speed defined in ICNC2.DLL, return speed in mm/mn
// else return 0;
DWORD _ICNC_GetCuttingSpeed(void); // mm/mn


//#define LANG_ENGLISH     0
//#define LANG_DEUTSCH     1
//#define LANG_FRANCAIS    2
//#define LANG_ITALIANO    3
DWORD _ICNC_SetLanguage(DWORD Language);

DWORD _ICNC_SetVerboseMode(DWORD Verbose);



// Receive cutting condition from GALAAD
DWORD _ICNC_SetTorchDownParams(DWORD ToolNumber,
                                 DWORD OriginZ,
                                 DWORD HeadUpZ,
                                 DWORD ProbeTorchOffsetZ,
                                 DWORD ProbingMarginZ,

                                 DWORD FastSpeedDownZ,
                                 DWORD ProbingSpeedZ,
                                 DWORD FastSpeedUpZ,
                                 DWORD ProbeInputNumber,
                                 DWORD ProbeInputState);
								 
								 
// **********************************  Fin de fonctions sp�cifiques GALAAD								 



// ********************************** Fonctions sp�cifiques MULTI CN
DWORD _ICNC_PlasmaSettingDlg (  double* HPercage, double* TPercage, double* HCoupe, double* Vitesse, double* THCVoltage, double* Intensite,
                                            int*  PalpageOne, int*  THCActif, int*  ControlePoste, int*  Simulation);


// ********************************** Fin de Fonctions sp�cifiques MULTI CN


// Passage de la carte en mode bootloader pour transfert d'une mise � jour firmware.
DWORD _ICNC_SwitchToBootLoaderMode (  DWORD BootKey);


EXTERN_C_END

#endif

