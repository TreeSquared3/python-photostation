from datetime import datetime, timezone

class PhotoStationUtils(object):
    @staticmethod
    def ascii2hex(str):
        return ''.join(format(ord(x), "x") for x in str)

    @staticmethod
    def hex2ascii(hex):
        return bytearray.fromhex(hex).decode('utf-8')


    @staticmethod
    def ymdhms_to_timestamp_utc(value: str) -> int:
        naive_dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        utc_dt = naive_dt.replace(tzinfo=timezone.utc)
        return int(utc_dt.timestamp())

    @staticmethod
    def album_id(path):
        if not path:
            return ''
        else:
            return 'album_' + PhotoStationUtils.ascii2hex(path)

    @staticmethod
    def album_path(album_id):
        return PhotoStationUtils.hex2ascii(album_id.split('_')[1])

    @staticmethod
    def photo_id(filetype, path, filename):
        return '_'.join((filetype, PhotoStationUtils.ascii2hex(path), PhotoStationUtils.ascii2hex(filename)))

    @staticmethod
    def photo_name(photo_id):
        return PhotoStationUtils.hex2ascii(photo_id.split('_')[2])

    # check if coordinates match within 0.01 degrees to prevent rounding issues
    @staticmethod
    def check_coordinates(coord1, coord2):
        if not coord1 or not coord2:
            return coord1 == coord2 
        return abs(float(coord1) - float(coord2)) < 0.01
