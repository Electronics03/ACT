from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/monitor", response_class=HTMLResponse)
def monitor():
    return r"""
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>콜센터 모니터</title>
  <style>
    body{
      margin:0;background:#050711;color:#e7eaf0;
      font-family:system-ui,-apple-system,"Noto Sans KR",sans-serif;
      display:flex;align-items:center;justify-content:center;min-height:100vh;
    }
    .monitor{
      width:1100px;height:620px;background:#0b0f19;border:1px solid rgba(255,255,255,.12);
      border-radius:18px;box-shadow:0 30px 80px rgba(0,0,0,.55);overflow:hidden;
    }
    .topbar{
      height:56px;display:flex;align-items:center;justify-content:space-between;padding:0 18px;
      border-bottom:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.03);
    }
    .pill{
      padding:6px 10px;border-radius:999px;border:1px solid rgba(255,255,255,.12);
      background:rgba(255,255,255,.04);font-size:12px;
    }
    .content{
      display:grid;grid-template-columns:1.2fr .8fr;height:calc(100% - 56px);
    }

    /* 좌/우 패널을 "세로로 쌓이게" */
    .left{
      padding:18px;border-right:1px solid rgba(255,255,255,.12);
      display:flex;flex-direction:column;gap:14px;min-height:0;
    }
    .right{
      padding:18px;
      display:flex;flex-direction:column;gap:14px;min-height:0;
    }

    .card{
      background:rgba(255,255,255,.06);
      border:1px solid rgba(255,255,255,.12);
      border-radius:16px;padding:14px;
    }
    .row{
      display:flex;justify-content:space-between;gap:12px;padding:10px 0;
      border-bottom:1px dashed rgba(255,255,255,.15);font-size:13px;
    }
    .row:last-child{border-bottom:0;}
    .k{opacity:.7;}
    .v{font-weight:700;}

    .sectionTitle{
      opacity:.7;font-size:12px;margin-bottom:8px;letter-spacing:.2px;
      display:flex;align-items:center;justify-content:space-between;gap:10px;
    }
    .miniBadge{
      font-size:11px;padding:4px 8px;border-radius:999px;
      border:1px solid rgba(255,255,255,.12);
      background:rgba(255,255,255,.04);
      opacity:.9;
    }

    .bigTimer{
      padding:18px;border-radius:16px;border:1px solid rgba(255,59,59,.35);
      background:rgba(255,59,59,.10);
    }
    #timer{
      font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;
      font-size:56px;font-weight:900;color:#ff3b3b;letter-spacing:1px;line-height:1;
      text-shadow:0 0 18px rgba(255,59,59,.28);
    }
    .blink{animation:blink .9s steps(2,start) infinite;}
    @keyframes blink{0%{opacity:1}50%{opacity:.25}100%{opacity:1}}
    .note{opacity:.75;font-size:12px;line-height:1.5;margin-top:10px;}

    /* 스크롤 영역 */
    .scrollArea{
      min-height:0;
      overflow:auto;
      padding-right:6px; /* 스크롤바 여유 */
    }
    .scrollArea::-webkit-scrollbar{width:8px;}
    .scrollArea::-webkit-scrollbar-thumb{background:rgba(255,255,255,.12);border-radius:999px;}
    .scrollArea::-webkit-scrollbar-track{background:transparent;}

    /* 대기명단 아이템 */
    .queueItem{
      display:flex;justify-content:space-between;gap:12px;
      padding:10px 0;border-bottom:1px dashed rgba(255,255,255,.15);
      font-size:13px;
    }
    .queueItem:last-child{border-bottom:0;}
    .queueLeft{display:flex;flex-direction:column;gap:4px;min-width:0;}
    .queueName{font-weight:800;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
    .queueMeta{opacity:.72;font-size:12px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
    .queueRight{display:flex;flex-direction:column;align-items:flex-end;gap:6px;flex:0 0 auto;}
    .queueTime{
      font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;
      opacity:.9;font-weight:800;
    }
    .prio{
      font-size:11px;padding:4px 8px;border-radius:999px;
      border:1px solid rgba(255,255,255,.12);
      background:rgba(255,255,255,.04);
    }
    .prio.high{border-color:rgba(255,184,77,.45);background:rgba(255,184,77,.12);color:#ffd39a;}
    .prio.urgent{border-color:rgba(255,59,59,.45);background:rgba(255,59,59,.12);color:#ffb2b2;}
    .dotWarn{
      width:8px;height:8px;border-radius:50%;
      background:#ff3b3b;box-shadow:0 0 14px rgba(255,59,59,.45);
      display:inline-block;margin-right:6px;
      animation: blink2 1.1s steps(2,start) infinite;
    }
    @keyframes blink2{0%{opacity:1}50%{opacity:.2}100%{opacity:1}}

    /* 내선 업무 톡 */
    .chatCard{flex:1;display:flex;flex-direction:column;min-height:0;}
    .chatList{flex:1;min-height:0;overflow:auto;padding-right:6px;}
    .chatList::-webkit-scrollbar{width:8px;}
    .chatList::-webkit-scrollbar-thumb{background:rgba(255,255,255,.12);border-radius:999px;}
    .msg{
      display:flex;flex-direction:column;gap:6px;margin:10px 0;
    }
    .msgHead{
      display:flex;justify-content:space-between;gap:10px;
      font-size:11px;opacity:.7;
    }
    .bubble{
      max-width: 92%;
      padding:10px 12px;border-radius:14px;
      border:1px solid rgba(255,255,255,.12);
      background:rgba(255,255,255,.05);
      font-size:13px;line-height:1.5;
      word-break:break-word;
    }
    .mine{align-items:flex-end;}
    .mine .bubble{
      background:rgba(124,92,255,.14);
      border-color:rgba(124,92,255,.32);
    }
    .sys .bubble{
      background:rgba(255,255,255,.03);
      border-style:dashed;
      opacity:.85;
    }
    .chatInput{
      margin-top:10px;
      border-top:1px solid rgba(255,255,255,.12);
      padding-top:10px;
      display:flex;gap:10px;align-items:center;
      opacity:.85;
    }
    .fakeInput{
      flex:1;
      padding:10px 12px;border-radius:12px;
      border:1px solid rgba(255,255,255,.12);
      background:rgba(255,255,255,.03);
      font-size:12px;opacity:.7;
    }
    .sendBtn{
      padding:10px 12px;border-radius:12px;
      border:1px solid rgba(255,255,255,.12);
      background:rgba(255,255,255,.05);
      font-size:12px;
    }
  </style>
</head>
<body>
  <div class="monitor">
    <div class="topbar">
      <div style="font-weight:800;font-size:14px;">토스 고객센터 · 상담 콘솔</div>
      <div style="display:flex;gap:10px;">
        <span class="pill">통화중</span>
        <span class="pill">010-1243-5234  &nbsp; 3F-12</span>
      </div>
    </div>

    <div class="content">
      <!-- LEFT -->
      <div class="left">
        <!-- 고객 정보 -->
        <div class="card">
          <div class="sectionTitle">
            <span>고객 정보</span>
            <span class="miniBadge">현재 콜</span>
          </div>
          <div class="row"><span class="k">이름</span><span class="v">권태환</span></div>
          <div class="row"><span class="k">최근 문의</span><span class="v">출금/이체 오류</span></div>
          <div class="row"><span class="k">메모</span><span class="v">--</span></div>
        </div>

        <!-- 대기명단 (추가) -->
        <div class="card" style="flex:1;display:flex;flex-direction:column;min-height:0;">
          <div class="sectionTitle">
            <span>대기 명단</span>
            <span class="miniBadge">Queue · 7</span>
          </div>

          <div id="queue" class="scrollArea" style="flex:1;">
            <div class="queueItem">
              <div class="queueLeft">
                <div class="queueName"><span class="dotWarn"></span>박상혁</div>
                <div class="queueMeta">카드 결제 취소 · “환불이 안 들어옴”</div>
              </div>
              <div class="queueRight">
                <div class="queueTime" data-wait="142">02:22</div>
                <div class="prio urgent">긴급</div>
              </div>
            </div>

            <div class="queueItem">
              <div class="queueLeft">
                <div class="queueName">김혜윤</div>
                <div class="queueMeta">계정 로그인 · 2FA 오류</div>
              </div>
              <div class="queueRight">
                <div class="queueTime" data-wait="88">01:28</div>
                <div class="prio high">높음</div>
              </div>
            </div>

            <div class="queueItem">
              <div class="queueLeft">
                <div class="queueName">배수홍</div>
                <div class="queueMeta">해외 결제 · 승인 거절</div>
              </div>
              <div class="queueRight">
                <div class="queueTime" data-wait="65">01:05</div>
                <div class="prio">보통</div>
              </div>
            </div>

            <div class="queueItem">
              <div class="queueLeft">
                <div class="queueName">조민서</div>
                <div class="queueMeta">송금 · 수취 실패(은행 점검?)</div>
              </div>
              <div class="queueRight">
                <div class="queueTime" data-wait="54">00:54</div>
                <div class="prio">보통</div>
              </div>
            </div>

            <div class="queueItem">
              <div class="queueLeft">
                <div class="queueName">김광민</div>
                <div class="queueMeta">대출 · 한도 조회 오류</div>
              </div>
              <div class="queueRight">
                <div class="queueTime" data-wait="43">00:43</div>
                <div class="prio">보통</div>
              </div>
            </div>

            <div class="queueItem">
              <div class="queueLeft">
                <div class="queueName">김상윤</div>
                <div class="queueMeta">현금영수증 · 발급 누락</div>
              </div>
              <div class="queueRight">
                <div class="queueTime" data-wait="31">00:31</div>
                <div class="prio">보통</div>
              </div>
            </div>

            <div class="queueItem">
              <div class="queueLeft">
                <div class="queueName">장서윤</div>
                <div class="queueMeta">자동이체 · 출금일 변경 문의</div>
              </div>
              <div class="queueRight">
                <div class="queueTime" data-wait="18">00:18</div>
                <div class="prio">보통</div>
              </div>
            </div>
          </div>
          
          <div class="note" style="margin-top:10px;">
            ※ 연출용: 대기시간이 1초씩 증가합니다.
          </div>
        </div>
      </div>

      <!-- RIGHT -->
      <div class="right">
        <!-- 통화 타이머 -->
        <div class="bigTimer">
          <div style="opacity:.75;font-size:12px;margin-bottom:10px;">통화 중 시간</div>
          <div id="timer" class="blink">00:00</div>
          <div class="note">Space: 일시정지 / R: 리셋</div>
        </div>

        <!-- 상담 상태 -->
        <div class="card">
          <div class="sectionTitle">
            <span>상담 상태</span>
            <span class="miniBadge">Agent: JASON</span>
          </div>
          <div class="row"><span class="k">우선순위</span><span class="v">높음</span></div>
          <div class="row"><span class="k">스크립트</span><span class="v">표준 안내</span></div>
        </div>

        <!-- 내선 업무 톡 (추가) -->
        <div class="card chatCard">
          <div class="sectionTitle">
            <span>내선 업무 톡</span>
            <span class="miniBadge">3F 운영 · LIVE</span>
          </div>

          <div id="chat" class="chatList">
            <div class="msg sys">
              <div class="msgHead"><span>시스템</span><span>방금</span></div>
              <div class="bubble">[공지] 금일 19:30~20:10 계좌이체 지연 가능성(모니터링 중)</div>
            </div>

            <div class="msg">
              <div class="msgHead"><span>슈퍼바이저(수진)</span><span>방금</span></div>
              <div class="bubble">출금/이체 오류 건 들어오면 “점검/지연” 안내 먼저. 폭언 심하면 즉시 기록.</div>
            </div>

            <div class="msg mine">
              <div class="msgHead"><span>나(3F-12)</span><span>방금</span></div>
              <div class="bubble">네. 현재 3F-12 통화중, 고객 감정 높음.</div>
            </div>
          </div>

          <div class="chatInput">
            <div class="fakeInput">메시지 입력</div>
            <div class="sendBtn">전송</div>
          </div>
        </div>
      </div>
    </div>
  </div>

<script>
  // ====== 통화 타이머 ======
  let sec = 0;
  let running = true;
  const timerEl = document.getElementById("timer");

  function fmt(n){
    const m = Math.floor(n / 60);
    const s = n % 60;
    return String(m).padStart(2,"0") + ":" + String(s).padStart(2,"0");
  }

  function tick(){
    if(!running) return;
    sec += 1;
    timerEl.textContent = fmt(sec);
    if (sec === 20) timerEl.style.animationDuration = "0.6s";
    if (sec === 40) timerEl.style.animationDuration = "0.45s";
  }
  setInterval(tick, 1000);

  window.addEventListener("keydown", (e) => {
    if (e.code === "Space") running = !running;
    if (e.key.toLowerCase() === "r") {
      sec = 0;
      timerEl.textContent = "00:00";
      timerEl.style.animationDuration = "0.9s";
    }
  });

  // ====== 대기명단: 대기시간 1초 증가 ======
  const queueEl = document.getElementById("queue");

  function updateQueueTimes(){
    const times = queueEl.querySelectorAll(".queueTime");
    times.forEach(t => {
      let w = parseInt(t.getAttribute("data-wait") || "0", 10);
      w += 1;
      t.setAttribute("data-wait", String(w));
      t.textContent = fmt(w);
    });
  }
  setInterval(updateQueueTimes, 1000);

  // ====== 내선 업무 톡: 자동 메시지 추가(연출용) ======
  const chatEl = document.getElementById("chat");

  const canned = [
    {who:"3F-07(민호)", text:"이체 지연 문의 폭주. 표준 멘트로 정리중."},
    {who:"슈퍼바이저(수진)", text:"폭언 심하면 ‘통화 종료 기준’ 적용해도 됨. 기록 남겨."},
    {who:"3F-02(지연)", text:"카드 환불 건은 PG 승인 시점 확인 먼저."},
    {who:"시스템", text:"[알림] 대기열 5명 이상. 콜백 유도 권장.", sys:true},
    {who:"3F-11(영재)", text:"현재 장애 티켓 #2411 업데이트 없음. 10분 뒤 재공지 예정."}
  ];

  function nowHHMM(){
    const d = new Date();
    const hh = String(d.getHours()).padStart(2,"0");
    const mm = String(d.getMinutes()).padStart(2,"0");
    return `${hh}:${mm}`;
  }

  function addMsg(who, text, mine=false, sys=false){
    const wrap = document.createElement("div");
    wrap.className = "msg" + (mine ? " mine" : "") + (sys ? " sys" : "");

    const head = document.createElement("div");
    head.className = "msgHead";
    const left = document.createElement("span");
    left.textContent = who;
    const right = document.createElement("span");
    right.textContent = nowHHMM();
    head.appendChild(left);
    head.appendChild(right);

    const bubble = document.createElement("div");
    bubble.className = "bubble";
    bubble.textContent = text;

    wrap.appendChild(head);
    wrap.appendChild(bubble);
    chatEl.appendChild(wrap);

    // 항상 아래로 스크롤(촬영용)
    chatEl.scrollTop = chatEl.scrollHeight;
  }

  let idx = 0;
  setInterval(() => {
    const m = canned[idx % canned.length];
    addMsg(m.who, m.text, false, !!m.sys);
    idx += 1;
  }, 4500);
</script>
</body>
</html>
"""


if __name__ == "__main__":
    import uvicorn

    # 파일명이 ACT_창.py 라는 전제 (현재 코드 그대로)
    uvicorn.run("ACT_창:app", host="127.0.0.1", port=8000, reload=True)
