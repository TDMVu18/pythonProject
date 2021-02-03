import webop
import fileop


def main():
    url = input('Nhập link khởi đầu: ')
    count = int(input('Nhập số lượng trang: '))
    waiting_line = webop.lay_cac_duong_link(webop.doc_noi_dung(url), url)
    history = webop.countlink(waiting_line, url, count)
    fileop.thumuc(input('Nhập tên thư mục lưu file: '))
    fileop.luufile(history, count)


if __name__ == '__main__':
    main()
