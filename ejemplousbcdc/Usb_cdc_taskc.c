#define __NO_UART__
#if defined(PIN_USB_SENSE)
   #define USB_CABLE_IS_ATTACHED() input(PIN_USB_SENSE)
#elif defined(__PCD__)
   #bit U1OTGSTAT_SESVD=getenv("BIT:SESVD")
   #define USB_CABLE_IS_ATTACHED() (U1OTGSTAT_SESVD)   
#endif
#include <string.h>
#DEFINE LED1 PIN_b0  //green
#define LED2 PIN_d1  //yellow
#define LED3 PIN_B5  //red
#define BUTTON_PRESSED() !input(PIN_A4)
#define LED_ON output_HIGH
#define LED_OFF output_low
#if defined(__NO_UART__)
   #define uart_putc(c)
   #define uart_getc()  (0)
   #define uart_kbhit() (FALSE)
   #define uart_printf(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) { }
   #define uart_task()
#else
   #ifndef __UART_BAUD__
      #define __UART_BAUD__   9600
   #endif
   #if defined(PIN_UART_TX)
      #use rs232(baud=__UART_BAUD__, xmit=PIN_UART_TX, rcv=PIN_UART_RX, errors)
   #else
      #use rs232(baud=__UART_BAUD__, UART1, errors)
   #endif

   #define uart_getc    getc
   #define uart_kbhit   kbhit
   #define uart_printf  printf

   #if defined(UART_USE_TX_BUFFER)
      char tbeBuffer[2750];
      unsigned int16 tbeIn=0, tbeOut=0, tbeCount=0;

      void uart_putc(char c)
      {
         if (tbeCount < sizeof(tbeBuffer))
         {
            tbeCount++;
            tbeBuffer[tbeIn++] = c;
            if (tbeIn >= sizeof(tbeBuffer))
               tbeIn = 0;
         }
      }

      void uart_task(void)
      {
         char c;
         if (tbeCount)
         {
            tbeCount--;
            c = tbeBuffer[tbeOut++];
            if (tbeOut >= sizeof(tbeBuffer))
               tbeOut = 0;
            putc(c);
         }
      }
   #else
      void uart_putc(char c) {putc(c);}
      #define uart_task()
   #endif
#endif
//#include "hid_boot.c"
/////////////////////////////////////////////////////////////////////////////
//
// usb_debug_task()
//
// When called periodically, displays debugging information over serial
// to display enumeration and connection states.  Also lights LED1 based upon
// enumeration and status.
//
/////////////////////////////////////////////////////////////////////////////
void usb_debug_task(void)
{
   static int8 last_connected;
   static int8 last_enumerated;
   int8 new_connected;
   int8 new_enumerated;
   static int8 last_cdc;
   int8 new_cdc;

   new_connected=usb_attached();
   new_enumerated=usb_enumerated();
   new_cdc=usb_cdc_connected();

   if (new_enumerated)
      LED_ON(LED1);
   else
      LED_OFF(LED1);

   if (new_cdc)
      LED_ON(LED2);
   else
      LED_OFF(LED2);

   if (usb_cdc_carrier.dte_present)
      LED_ON(LED3);
   else
      LED_OFF(LED3);

   if (new_connected && !last_connected)
      uart_printf("USB connected, waiting for enumaration...\r\n\n");
   if (!new_connected && last_connected)
      uart_printf("USB disconnected, waiting for connection...\r\n\n");
   if (new_enumerated && !last_enumerated)
      uart_printf("USB enumerated by PC/HOST\r\n\n");
   if (!new_enumerated && last_enumerated)
      uart_printf("USB unenumerated by PC/HOST, waiting for enumeration...\r\n\n");
   if (new_cdc && !last_cdc)
      uart_printf("Serial program initiated on USB<->UART COM Port\r\n\n");

   last_connected=new_connected;
   last_enumerated=new_enumerated;
   last_cdc=new_cdc;
}

// transmit to the host new dcd/dsr, it's value based on button.
void cdc_serial_state_task(void)
{
   cdc_serial_state_t newState;
   static cdc_serial_state_t lastState;

   memset(&newState, 0x00, sizeof(newState));

   newState.bRxCarrier = BUTTON_PRESSED();
   newState.bTxCarrier = newState.bRxCarrier;

   if (memcmp(&newState, &lastState, sizeof(newState)) != 0)
   {
      uart_printf("\r\nNew button state being sent: ");
      //change in state, send it.
      if (usb_cdc_serial_state(newState))
      {
         //state was sent ok, save it in memory so we don't resend it.
         memcpy(&lastState, &newState, sizeof(lastState));
         uart_printf("OK");
      }
      else
      {
         uart_printf("FAIL");
      }
      uart_printf("\r\n");
   }
}
#ifndef HW_INIT
#define HW_INIT()
#endif

