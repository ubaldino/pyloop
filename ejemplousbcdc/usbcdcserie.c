
#include "Sawerspic.c"
#include <usb_cdc.h>
#include <usb_cdc_taskc.c> 

void main(void)
{
   char c;

   HW_INIT();

   LED_OFF(LED1);
   LED_OFF(LED2);
   LED_OFF(LED3);    
   // init USB (non-blocking)
   // usb_task() need to be called in your loop to finish USB initialization.
   usb_init_cs();
   while (TRUE)
   {
      usb_task();
      usb_debug_task();
      cdc_serial_state_task();
      if (usb_cdc_kbhit())
      {
         c=usb_cdc_getc();
         usb_cdc_putc(c);
         if(c=='A')
            printf(usb_cdc_putc,"hola mudo");
         if(c == '1')
            output_low(pin_D0);
         if(c == '2')
            output_high(pin_D0);
      }
      
   }
}

