#include <gusb.h>

#include <glib.h>
#include <glib-object.h>

int main (int argc, char *argv[])
{
  GError *error = NULL;
  GUsbContext *context = NULL;

  context = g_usb_context_new (&error);

  if (context == NULL)
    g_error ("%s", error->message);

  g_object_unref (context);
  return 0;
}
