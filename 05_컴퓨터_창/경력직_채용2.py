from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/tongyang-pass", response_class=HTMLResponse)
def tongyang_pass():
    return """
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>TONGYANG Careers | 경력직 결과 확인</title>
  <style>
    :root{
      --dark0:#050711;
      --dark1:#0b0f19;
      --line:rgba(255,255,255,.10);
      --text:#e7eaf0;
      --muted:rgba(231,234,240,.70);

      /* ✅ 포인트 컬러: 파랑 */
      --tongyang:#2b6cff;

      --lightBg:#f6f7fb;
      --lightCard:#ffffff;
      --lightText:#10131a;
      --lightMuted:rgba(16,19,26,.65);
    }

    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      font-family:system-ui,-apple-system,"Noto Sans KR",sans-serif;
      overflow:hidden;
    }

    .page{
      min-height:100vh;
      display:flex;
      align-items:center;
      justify-content:center;
      background: radial-gradient(1200px 700px at 20% 10%, #151a2d, var(--dark0));
      color:var(--text);
      position:relative;
    }

    .lightLayer{
      position:absolute; inset:0;
      background: radial-gradient(1200px 700px at 20% 10%, #ffffff, var(--lightBg));
      opacity:0;
      transition: opacity 900ms cubic-bezier(.2,.9,.2,1);
    }
    .page.revealed .lightLayer{opacity:1;}

    .wrap{width:min(980px, 92vw); position:relative; z-index:1; padding:28px 0;}

    .card{
      background: rgba(11,15,25,.92);
      border:1px solid var(--line);
      border-radius:18px;
      box-shadow:0 30px 80px rgba(0,0,0,.55);
      overflow:hidden;
      transform: translateZ(0);
      transition:
        transform 900ms cubic-bezier(.2,.9,.2,1),
        box-shadow 900ms cubic-bezier(.2,.9,.2,1),
        background 900ms cubic-bezier(.2,.9,.2,1),
        border-color 900ms cubic-bezier(.2,.9,.2,1),
        color 900ms cubic-bezier(.2,.9,.2,1);
    }

    .page.revealed .card{
      background: rgba(255,255,255,.92);
      border-color: rgba(16,19,26,.10);
      color: var(--lightText);
      box-shadow: 0 26px 70px rgba(0,0,0,.18);
    }
    .card.zoom{ transform: scale(1.08); }

    .top{
      padding:18px 18px 14px 18px;
      display:flex;
      gap:16px;
      align-items:flex-start;
      justify-content:space-between;
      flex-wrap:wrap;
    }

    .brand{display:flex; gap:12px; align-items:center}
    .badge{
      width:44px;height:44px;border-radius:12px;
      display:inline-flex;align-items:center;justify-content:center;
      background: color-mix(in srgb, var(--tongyang) 18%, transparent);
      border:1px solid color-mix(in srgb, var(--tongyang) 35%, transparent);
      color: var(--tongyang);
      font-weight:900;
      letter-spacing:.5px;
      text-transform:uppercase;
    }
    .brandTitle{font-weight:900; font-size:16px; line-height:1.2}
    .brandSub{font-size:12.5px; color:var(--muted); margin-top:2px}
    .page.revealed .brandSub{ color: var(--lightMuted); }

    .meta{display:flex; flex-direction:column; gap:8px; align-items:flex-end}
    .metaRow{display:flex; gap:8px; align-items:center; font-size:12.5px; color:var(--muted)}
    .page.revealed .metaRow{ color: var(--lightMuted); }

    .dot{width:7px;height:7px;border-radius:50%; background:rgba(255,255,255,.35)}
    .page.revealed .dot{ background: rgba(16,19,26,.25); }

    .pill{
      font-size:12px;
      padding:6px 10px;
      border-radius:999px;
      border:1px solid rgba(255,255,255,.14);
      background: rgba(255,255,255,.04);
      color: rgba(231,234,240,.85);
    }
    .page.revealed .pill{
      border:1px solid rgba(16,19,26,.10);
      background: rgba(16,19,26,.03);
      color: rgba(16,19,26,.80);
    }

    .divider{height:1px; background: rgba(255,255,255,.10);}
    .page.revealed .divider{ background: rgba(16,19,26,.10); }

    .content{padding:22px 18px 20px 18px;}
    h1{margin:0 0 10px 0; font-size:22px; letter-spacing:-.2px;}
    p{margin:0 0 18px 0; color:var(--muted); line-height:1.6;}
    .page.revealed p{ color: var(--lightMuted); }

    .btn{
      width:100%;
      border:0;
      padding:14px 14px;
      border-radius:14px;
      background: var(--tongyang);
      color:#fff;
      font-weight:900;
      font-size:15px;
      cursor:pointer;
      transition: transform 140ms ease;
    }
    .btn:active{ transform: scale(.99); }

    .btnGhost{
      width:100%;
      border:1px solid rgba(255,255,255,.16);
      padding:14px 14px;
      border-radius:14px;
      background: transparent;
      color: var(--text);
      font-weight:900;
      font-size:15px;
      cursor:pointer;
    }
    .page.revealed .btnGhost{
      border:1px solid rgba(16,19,26,.12);
      color: var(--lightText);
    }

    .result{position:relative; padding-top:6px; display:none;}
    .page.revealed .result{display:block; animation: pop 520ms cubic-bezier(.2,.9,.2,1) both;}
    .page.revealed .pre{display:none;}

    .stamp{
      position:absolute; right:0; top:-10px;
      font-weight:900; letter-spacing:2px;
      padding:10px 12px;
      border-radius:12px;
      border:2px solid color-mix(in srgb, var(--tongyang) 45%, transparent);
      color: var(--tongyang);
      background: color-mix(in srgb, var(--tongyang) 6%, transparent);
      transform: rotate(8deg);
    }
    .passTitle{margin:0 0 8px 0; font-size:34px; letter-spacing:-.8px; font-weight:950;}
    .passSub{margin:0 0 16px 0; color: var(--lightMuted); line-height:1.6;}

    .resultBox{
      border-radius:16px;
      border:1px solid rgba(16,19,26,.10);
      background: rgba(16,19,26,.03);
      padding:14px 14px;
      display:flex;
      flex-direction:column;
      gap:10px;
      margin-bottom:14px;
    }

    .row{display:flex; justify-content:space-between; gap:14px; font-size:14px;}
    .k{color: rgba(16,19,26,.62); white-space:nowrap;}
    .v{color: rgba(16,19,26,.92); text-align:right;}
    .strong{font-weight:950; color:#0a0a0a;}

    .actions{display:flex; gap:10px;}
    .actions > button{flex:1}

    @keyframes pop{
      from{ transform: translateY(10px); opacity:0; }
      to{ transform: translateY(0); opacity:1; }
    }
  </style>
</head>

<body>
  <div class="page" id="page">
    <div class="lightLayer" aria-hidden="true"></div>

    <main class="wrap">
      <section class="card" id="card">
        <header class="top">
          <div class="brand">
            <span class="badge" aria-hidden="true">TY</span>
            <div class="brandText">
              <div class="brandTitle">TONGYANG Careers</div>
              <div class="brandSub">경력직 채용 결과 확인</div>
            </div>
          </div>

          <div class="meta">
            <div class="metaRow">
              <span class="dot"></span>
              <span id="dt"></span>
            </div>
            <div class="metaRow">
              <span class="pill">경력</span>
              <span class="pill">생산/품질</span>
              <span class="pill">면접 전형</span>
            </div>
          </div>
        </header>

        <div class="divider"></div>

        <div class="content">
          <div class="pre">
            <h1>2차면접 결과</h1>
            <p>
              본 페이지에서 경력직 채용 전형 결과를 확인할 수 있습니다.<br/>
              아래 버튼을 눌러 결과를 확인해 주세요.
            </p>
            <button class="btn" id="revealBtn">합격 확인</button>
          </div>

          <div class="result" aria-live="polite">
            <div class="stamp" aria-hidden="true">PASS</div>
            <h1 class="passTitle">합격입니다</h1>
            <p class="passSub">
              축하드립니다.<br/>
              TONGYANG 경력직 채용 전형에 최종 합격하셨습니다.
            </p>

            <div class="resultBox">
              <div class="row"><span class="k">지원분야</span><span class="v">생산/품질 (경력)</span></div>
              <div class="row"><span class="k">결과</span><span class="v strong">최종 합격</span></div>
              <div class="row"><span class="k">안내</span><span class="v">추후 절차는 이메일/문자 안내 예정</span></div>
            </div>

            <div class="actions">
              <button class="btnGhost" id="resetBtn">다시 보기</button>
              <button class="btn" id="okBtn">확인</button>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>

  <script>
    const page = document.getElementById("page");
    const card = document.getElementById("card");
    const dt = document.getElementById("dt");
    const revealBtn = document.getElementById("revealBtn");
    const resetBtn = document.getElementById("resetBtn");
    const okBtn = document.getElementById("okBtn");

    const now = new Date();
    const pad = (n) => String(n).padStart(2, "0");
    dt.textContent = `${now.getFullYear()}-${pad(now.getMonth()+1)}-${pad(now.getDate())} 23:00`;

    function reveal(){
      page.classList.add("revealed");
      card.classList.add("zoom");
    }
    function reset(){
      page.classList.remove("revealed");
      card.classList.remove("zoom");
    }

    revealBtn.addEventListener("click", reveal);
    resetBtn.addEventListener("click", reset);
    okBtn.addEventListener("click", () => alert("축하합니다! (데모)"));
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
