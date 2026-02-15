from machine import UART
from time import sleep_ms

class Nextion:
    END_COMMAND = b"\xff\xff\xff"
    PAGE_NUMBER_VERIFICATION = b"#\x02P"

    def __init__(self, baudrate, tx=10, rx=9, get_page_event=False, start_page=0):
        """
        UART channel is 1.

        :param baudrate: Check out the display's instructions. E.g. 9600
        :param tx: The tx-Pin you want to use.
        :param rx: The rx-Pin you want to use.
        :param get_page_event: If True, it detects page switching.To do this,
            you have to write the preinitialize event for each page:
            `printh 23 02 50 xx`. `xx` is the page number in hex.
            For page 0: `printh 23 02 50 00`. For page 10: `printh 23 02 50 0A`.
            Now you can get the current page with `Nextion.current_page`.
            You can also set locked page with `Nextion.lock_pages.add(<page number>)`
        :param start_page: If the first displayed page isn't page-id 0, set them here.
            This is needed for `get_page_event`
        """
        self.uart = UART(1, baudrate, tx=tx, rx=rx)
        if get_page_event:
            self.uart.irq(handler=self._manage_next_page, trigger=UART.IRQ_RXIDLE)
            self.current_page = start_page
            self.buffer = bytearray()
            self.lock_pages = set()

    def _manage_next_page(self):
        self.uart.readinto(self.buffer, nbytes=4)
        if len(self.buffer) == 4 and self.buffer[:3] == self.PAGE_NUMBER_VERIFICATION:
            page = self.buffer[:3].hex()
            if page in self.lock_pages:
                self.change_page(self.current_page)
            else:
                self.current_page = int(self.buffer[3:].hex())
        self.buffer = bytearray()

    def change_page(self, page):
        """
        Change the page of the display.

        :param page: The name or the id of the page
            you want to go to.
        :return: None
        """
        self.cmd(f"page {page}")

    def cmd(self, command, write_and_read=True):
        """
        Send one of the Nextion-specific commands to the display.
        See: https://nextion.tech/instruction-set/

        :param command: The command you want to send
        :param write_and_read: If True(default), return a `UART.read()` object
            else return None
        :return: UART.read() or None
        """
        self.uart.write(command)
        self.uart.write(self.END_COMMAND)
        if write_and_read:
            sleep_ms(100)
            return self.uart.read()
        return None

    def sleep(self, state):
        """
        Sets display in sleep or awake mode

        :param state: If True, sleep-mode is on, else sleep-mode is off
        :return: None
        """
        self.cmd(f"sleep={state}")

    def reset(self):
        """
        Resets the Display
        """
        self.cmd("rest")

    def brightness(self, brightness):
        """
        Dim the display

        :param brightness: Values from 0...100
        :return: None
        """
        self.cmd(f"dim={brightness}")

    def read(self, raw=False):
        """
        Read the rx-line.

        :param raw: If True, the raw values are returned without decoding.
            If False (default), the values are decoded to `ascii`
        :return: UART.read() decoded or not. None if there aren't values
            of if there is an error while decoding.
        """
        output = self.uart.read()
        if raw:
            return output
        try:
            return output.decode("ascii")
        except AttributeError:
            return None
