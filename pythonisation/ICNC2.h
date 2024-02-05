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
// des accès aux fonctions de la DLL
// Input : TRUE pour passer en mode simulation
//
DWORD _ICNC_SetSimulationMode( BOOL  SimulationModeVal);

// Initialisation de la communication avec la carte InterpCNC
DWORD _ICNC_Connect( DWORD ICNC_Number);


// Definition de l'ID application
DWORD _ICNC_SetUserApplicationID( DWORD lUserApplicationID);

// Arrêt de la communication avec la carte InterpCNC
DWORD _ICNC_Disconnect( void);

// Dévérouillage carte
// Acquittemement Arrêt d'urgence, Fin de course
// Input : Bits de défauts à remettre à 0
//                ICNC_STATUS_BIT_EMERGENCYSTOP
//                ICNC_STATUS_BIT_LOCKED
//                ICNC_STATUS_BIT_HOMING_ERROR
//                ICNC_STATUS_BIT_PROBING_ERROR
//                ICNC_STATUS_BIT_WAIT_INPUT_ERROR
//                ICNC_STATUS_BIT_EEWRITE_ERROR)
// Output :
//      ICNCUSB_SUCCESS si communication ok
DWORD _ICNC_ErrorReset( DWORD ErrorBits);


// Commande NON bufferisées
// ********************

// Lecture du status de la carte. Il est possible de lire toutes les informations
// d'état interne de la carte par un seul appel à cette fonction.
// Pour éviter de surcharger la communication, faite une demande approriée en fonction
// des informations nécéssaire à l'instant donné.
// Input :
//        StatusType : combinaison des bits d'état à lire
//                    (exemple : ICNC_STATUS_BOARD_STATUS | ICNC_STATUS_BUFFER_FREE
// Output :
//       Status : pointeur sur une zone mémoire permettant le stockage de tous les
//                 états demandés.
// Result :  ICNCUSB_SUCCESS si communication ok
//
// Exemple1 : Lecture simultanée du status de la carte, de la place disponible dans le buffer
//            et de la position actuelle des axes X, Y et Z
//
//  Status DWORD[5];
//  ICNC_GetBoardStatus( ICNC_STATUS_BOARD_STATUS | ICNC_STATUS_BUFFER_FREE
//                         | ICNC_STATUS_ACTUALX | ICNC_STATUS_ACTUALY | ICNC_STATUS_ACTUALZ,
//                         &Status);
DWORD _ICNC_GetBoardStatus(DWORD StatusType,         // Input
                             DWORD *Status);           // Output

// Forcage de l'état des sorties
// Entrée :
//      OutputState = bits de sorties à activer
DWORD _ICNC_SetOutputAll(DWORD OutputState);

// Ecriture de la valeur de survitesse appliquée sur les commandes de déplacement.
// Input : OverrideValue = Sur vitesse en % de la vitesse de déplacement en cours.
DWORD _ICNC_SetOverrideValue(DWORD OverrideValue); // Input

// Lecture de la valeur actuelle d'override
DWORD _ICNC_GetOverrideValue(DWORD *OverrideValue); // Outpur

// Lancement d'une procédure de palpage sur un axe
// Entrées :
//        DWORD Axe : axe concerné (AXE_X ou AXE_Y...)
//        DWORD Direction : 0 si négative, 1 si positive
//        DWORD InNo : N° de l'entrée du palpeur
//        BOOL InValue : Valeur attendue sur le palpeur (0 ou 1)
//        DWORD MaxStroke : course maximum de recherche du palpeur
//        DWORD Speed : Vitesse de déplacement vers le capteur
//        DWORD FStart : Fréquence de démarrage de l'axe  (Hz)
//        DWORD Accel : Accélération  (KHz/s)
//        DWORD Decel : Décéleration  (KHz/s)
//
// L'utilisation de cette fonction pour le palpage permet de continuer le dialogue avec la carte durant l'opération de palpage.
// Durant cette opération, il est ainsi possible de lire les status de la carte pour affichage.
// Le bit de status ICNC_STATUS_BIT_PROBING reste à 1 tant que l'opération n'est pas terminée.
// Lorsque l'opération est terminée, le bit ICNC_STATUS_BIT_PROBING passe à 0.
// Il est alors nécéssaire de tester le bit de status ICNC_STATUS_BIT_PROBING_ERROR pour déterminer si l'opération s'est déroulée correctement.
// Si tel est le cas, la position de l'axe au moment de la detection du contact peut être lue par l'interrogation de status
// avec la demande ICNC_STATUS_LAST_PROBE
DWORD _ICNC_Probe(DWORD Axe, DWORD Direction, DWORD InNo, BOOL InValue, DWORD MaxStroke, DWORD Speed, DWORD FStart, DWORD Accel, DWORD Decel);

// Lancement d'une procédure de palpage sur un axe et attente du résultat
// Fonctionnement identique à la fonction ICNC_Probe mais bloquante jusqu'à l'obtention du résultat
// Entrées :
//        DWORD Axe : axe concerné (AXE_X ou AXE_Y...)
//        DWORD Direction : 0 si positive, 1 si négative
//        DWORD InNo : N° de l'entrée du palpeur
//        BOOL InValue : Valeur attendue sur le palpeur (0 ou 1)
//        DWORD MaxStroke : course maximum de recherche du palpeur
//        DWORD Speed : Vitesse de déplacement vers le capteur
//        DWORD FStart : Fréquence de démarrage de l'axe
//        DWORD Accel : Accélération
//        DWORD Decel : Décéleration
//  Sortie :
//        INT* ProbePosition : Position de l'axe lors de la détection du palpeur
//  Resultat :
//      ICNCUSB_SUCCESS si l'opération s'est déroulé correctement
//      ICNCUSB_PROBE_ERROR si erreur de paramètre ou palpeur non trouvée dans la course indiquée
//      ICNCUSB_FAIL si erreur de communication
DWORD _ICNC_ProbeAndReadBack(DWORD Axe, DWORD Direction, DWORD InNo, BOOL InValue, DWORD MaxStroke, DWORD Speed, DWORD FStart, DWORD Accel, DWORD Decel, INT* ProbePosition);

// Arrêt avec rampe des axes indiqués
DWORD _ICNC_SlowStopMotors(DWORD Axis);

// Arrêt avec rampe et vidage buffer
DWORD _ICNC_SlowStopAllAndClear(void);

// Arrêt sans rampe et vidage buffer
DWORD _ICNC_StopMotorsAllAndClear(void);

// Lecture de l'état des sorties
DWORD _ICNC_GetOutputAll(DWORD *OutputState); // Output

// Lecture de l'état d'une des entrées
DWORD _ICNC_GetInput( DWORD InNo, // Input
                        BOOL *InputState);

// Lecture de toutes les entrées
DWORD _ICNC_GetInputAll(  DWORD *InputState); // Output

// Lecture d'une entrée analogique
DWORD _ICNC_GetAnalog(   DWORD AnalogNo, // Input
                           DWORD *AnalogValue);

// Set de l'état d'une sortie
DWORD _ICNC_SetOutput(   DWORD OutputNo,
                            BOOL OutputState);

// Set de l'état d'une sortie analogique
// Entrées :
//      AnalogNo : Numéro de l'entrée analogique : ICNC_ANALOG1 ou ICNC_ANALOG2...
//      AnalogValue :  résolution de l'ADC obtenue par   ICNC_GetSysInfo( ICNC_SYS_INFO_ADC_RESOLUTION )
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

// Dévérouillage du traitement du buffer
// forcer le dédblocage du buffer pour exécuter les commande présentes.
// A utiliser en conjonction avec la fonction ICNC_FreezeBuf lors de la gestion
// de la cinématique à l'aide de micro vecteurs
//
DWORD _ICNC_Unfreeze(void);

// Ecriture non bufferisée d'une des cellules mémoire utilisateur
// Memory number = 0 à 9
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

// Lecture d'un paramètre carte. Voir définition dans GLOBALDEF.H
DWORD _ICNC_ReadParameter( DWORD ParameterID,
                             INT *ParameterValue);

// Ecriture d'un paramètre carte
// Par défaut, cette fonction attends et vérifie l'écriture du paramètre dans un temps limité de 1000ms
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


// Lancement d'une procédure d'origine d'un ou plusieurs axes
// Entrées :
//      DWORD Axis : Axes concernés (AXE_X | AXE_Y ...)
//
// Cette fonction n'est pas bloquante. Il est donc possible de communiquer avec la carte durant la prise d'origine
// Durant le traitement de cette fonction, le bit de status ICNC_STATUS_BIT_HOMING est à 1
// Lorsque ce bit passe à 0, interroger le bit de status ICNC_STATUS_BIT_HOMING pour déterminer si
// le traitement s'est déroulé correctement.
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



// Fonction spécifique pour machine de découpe plasma
DWORD _ICNC_SetTHCTarget( DWORD THCTargetValue);

// Non utilisé
DWORD _ICNC_ConfigPrompt( BOOL PromptState);

DWORD _ICNC_SetUSBSpeedMode( BOOL EnableHighSpeed);

// Lecture des informations systems de la carte.
// Entrées :
//      DWORD SysInfoType : bits indiquant les informations à lire
//                      (voir définition des bits ICNC_SYS_INFO_xxxxxxx)
// Sortie :
//      DWORD *SysInfo : structure contenant les résultats des informations demandées
DWORD _ICNC_GetSysInfo( DWORD SysInfoType,
                          DWORD *SysInfo);



// Lancement d'un mouvement indépendent sur un axe.
// Si un mouvement est déjà en cours, la nouvelle position cible est mise à jour.
// Le profile de vitesse est alors recalculé pour s'adapter à la nouvelle cible.
// Si l'axe est déjà en mouvement et la cible inchangée, la commande prend en compte la nouvlle vitesse et le profile est ajusté.

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


// Modification en dynamique d'un mouvement lancé avec la commande de déplacement anynchrone.
// Si l'axe n'est pas en mouvement, la commande est ignorée.
// Les modifications de vitesses se font en respectant les rampes d'accel et de decel indiquée par la commande de déplacement
// La commande prend effet immédiatement et n'est donc pas bufferisée.
DWORD _ICNC_UpdateSpeed( DWORD Axe,
                                   DWORD NewFrenquency);


								   
// Fonction non implémentée
DWORD _ICNC_RampUpAbsBuf( DWORD Axis,
                         INT Position[5],
                         DWORD FStart[5],
                         DWORD FEnd[5],
                         DWORD Accel[5]); // Hz/s

// Fonction non implémentée
DWORD _ICNC_RampDownAbsBuf( DWORD Axis,
                         INT Position[5],
                         DWORD FStart[5],
                         DWORD FEnd[5],
                         DWORD Decel[5]);  // Hz/s


// Activation/desactivation logiciel du THC
// La commande peut être bufferisée ou directe
// Note : Si le logciel doit prendre en charge l'activationdésactivation du THC, mettre
// le parammètre EE_THC_ACTIVATION_OUTPUT à 0 pour éviter les conflicts
DWORD _ICNC_SetTHCStateBuf(BOOL EnableTHC,
                          BOOL BufferizedCommand);




// Commande bufferisées
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

// Attentre l'état d'une entrée
// L'exécution du buffer de commande est gelé en attendant l'entrée concernée
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


// Ecriture non bufferisée d'une des cellules mémoire utilisateur
// Memory number = 0 à 9
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
// Déplacement relatif dans profile (vitesse constante) utilisant un buffer local
// sur le PC afin d'envoyer des trames complètes sur la cartee et optimiser le flux de communication USB
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
// Déplacement à une position absolue avec profile (trapézoïdale) utilisant un buffer local
// sur le PC afin d'envoyer des trames complètes sur la cartee et optimiser le flux de communication USB

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
// Déplacement à une position absolue sans profile (vitesse constante) utilisant un buffer local
// sur le PC afin d'envoyer des trames complètes sur la cartee et optimiser le flux de communication USB
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

// Vidage du buffer local PC et envoie à la carte.
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

							
							
// Envoie d'un tableau de pulses/direction à la carte
// Codage : Les octets du buffer peuvent êtres des affectations de sens de rotation ou des pulses sur les sorties CLK.
// 			Octet de direction : 0x40 | DIRECTION   avec DIRECTION = état des 5 sorties de direction
//			Octet de pas       : 0x20 | PULSES		avec PULSES qui indique sur quels sortie CLK générer des pulses
// Exemple : [0x41, 0x21, 0x23, 0x21]  aura pour effet d'activer la sortie DIR1 et de générer 3 pas sur CLK1 et 1 pas sur CLK2
// La fréquence de traitement du tableau étant indiquée dans le paramètre Frequency

DWORD _ICNC_PushPulsesData ( unsigned char *ptBuffer, 
										 int nbBytes, 
										 DWORD Frequency, 
										 #ifndef _MSC_VER
											DWORD *BufferRequired=NULL
										#else
											DWORD *BufferRequired
										#endif
										);

							
// **********************************  Fonctions spécifiques GALAAD								 


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
								 
								 
// **********************************  Fin de fonctions spécifiques GALAAD								 



// ********************************** Fonctions spécifiques MULTI CN
DWORD _ICNC_PlasmaSettingDlg (  double* HPercage, double* TPercage, double* HCoupe, double* Vitesse, double* THCVoltage, double* Intensite,
                                            int*  PalpageOne, int*  THCActif, int*  ControlePoste, int*  Simulation);


// ********************************** Fin de Fonctions spécifiques MULTI CN


// Passage de la carte en mode bootloader pour transfert d'une mise à jour firmware.
DWORD _ICNC_SwitchToBootLoaderMode (  DWORD BootKey);


EXTERN_C_END

#endif

