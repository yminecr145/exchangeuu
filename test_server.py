#!/usr/bin/env python3
"""
로컬에서 index.html을 즉시 미리보기할 수 있는 간이 테스트 서버입니다.
사용법: python3 test_server.py
"""

import http.server
import socketserver
import os
import webbrowser

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == '__main__':
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 60)
        print(f"🚀 부산대 교환학생 필터 로컬 테스트 서버가 시작되었습니다!")
        print(f"👉 브라우저 주소: {url}")
        print(f"종료하려면 터미널에서 Ctrl + C 를 누르세요.")
        print("=" * 60)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n서버가 종료되었습니다.")
