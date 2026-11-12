# 작업 규칙

- 이 저장소는 claude.ai 아티팩트 "내 프로그램 모음"(https://claude.ai/artifact/USjTTJV1aN4wP1zFSPuf1i, slug de3e80a8-436f-4f08-b2fb-ff37e91d69a1)의 공개판이다. 같은 index.html이 claude.ai에서는 전체·편집 화면, 여기(window.claude 없음)에서는 외부 공개 프로그램만 보이는 읽기 전용 화면으로 동작한다.
- 카드 제목·상태·설명 편집 내용은 아티팩트 db의 `portal/overrides` 문서(items)에 있다. 공개판에 반영할 때는 그 items를 JSON 파일로 받아 `python3 build_public.py items.json` → `public/index.html`을 이 저장소 index.html로 올린다(BAKED 자리에 굳혀 넣음).
- 카드 추가·링크·분류 변경 같은 코드 수정은 아티팩트와 이 저장소를 같이 갱신한다. 커밋 메시지에 아티팩트 버전 번호를 적는다.
- claude.ai 링크는 공개 화면에서 자동으로 숨겨진다. 🔒 내 전용(access 'me')·⏳ 공개 예정 카드는 공개 화면에 나오지 않는다.
- 응답은 한국어.
