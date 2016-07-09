from datetime import datetime
from time import sleep


class BinaryTime:
    @staticmethod
    def int_to_bin_list(i: int) -> list:
        bin_time = [0, 0, 0, 0]
        if i >= 8:
            bin_time[3] = 1
            i -= 8
        if i >= 4:
            bin_time[2] = 1
            i -= 4
        if i >= 2:
            bin_time[1] = 1
            i -= 2
        if i >= 1:
            bin_time[0] = 1
        return bin_time

    def __init__(self, h: int, m: int, s: int):
        #                [1, 2, 4, 8]
        self.hour_tens = self.int_to_bin_list(h // 10)
        self.hour_ones = self.int_to_bin_list(h % 10)
        self.minute_tens = self.int_to_bin_list(m // 10)
        self.minute_ones = self.int_to_bin_list(m % 10)
        self.second_tens = self.int_to_bin_list(s // 10)
        self.second_ones = self.int_to_bin_list(s % 10)


class Display:
    @staticmethod
    def bin_time_to_str(bin_time: BinaryTime) -> str:
        bin_str = ""
        bin_str_tmpl = \
            "[{ht}][{ho}][{mt}][{mo}][{st}][{so}]\n"

        ht = bin_time.hour_tens
        ho = bin_time.hour_ones
        mt = bin_time.minute_tens
        mo = bin_time.minute_ones
        st = bin_time.second_tens
        so = bin_time.second_ones

        for i in range(3, -1, -1):
            bin_str += bin_str_tmpl.format(
                ht=ht[i],
                ho=ho[i],
                mt=mt[i],
                mo=mo[i],
                st=st[i],
                so=so[i]
            )
        return bin_str \
            .replace("0", " ") \
            .replace("1", "X")


class BinaryClock:
    def run(self):
        while True:
            # get current time
            current_time = datetime.now()
            # convert to bin time
            current_time_bin = BinaryTime(current_time.hour, current_time.minute, current_time.second)
            # display bin time
            current_time_str = Display.bin_time_to_str(current_time_bin)
            print(current_time_str)
            sleep(1)


if __name__ == '__main__':
    bin_clock = BinaryClock()
    bin_clock.run()
