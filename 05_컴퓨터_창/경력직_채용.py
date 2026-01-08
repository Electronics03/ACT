import React, { useMemo, useState } from "react";

export default function KiaCareerPassCheck() {
  const [revealed, setRevealed] = useState(false);

  const today = useMemo(() => {
    const d = new Date();
    const yy = d.getFullYear();
    const mm = String(d.getMonth() + 1).padStart(2, "0");
    const dd = String(d.getDate()).padStart(2, "0");
    return `${yy}-${mm}-${dd}`;
  }, []);

  return (
    <div className={`page ${revealed ? "revealed" : ""}`}>
      {/* Light layer (dark -> light) */}
      <div className="lightLayer" aria-hidden="true" />

      <main className="wrap">
        <section className={`card ${revealed ? "cardZoom" : ""}`}>
          <header className="top">
            <div className="brand">
              <span className="badge" aria-hidden="true">KIA</span>
              <div className="brandText">
                <div className="brandTitle">KIA Careers</div>
                <div className="brandSub">경력직 채용 결과 확인</div>
              </div>
            </div>

            <div className="meta">
              <div className="metaRow">
                <span className="dot" />
                <span>{today} 23:00</span>
              </div>
              <div className="metaRow">
                <span className="pill">경력</span>
                <span className="pill">생산/품질</span>
                <span className="pill">면접 전형</span>
              </div>
            </div>
          </header>

          <div className="divider" />

          <div className="content">
            {!revealed ? (
              <>
                <h1 className="h1">2차면접 결과</h1>
                <p className="p">
                  본 페이지에서 경력직 채용 전형 결과를 확인할 수 있습니다. <br />
                  아래 버튼을 눌러 결과를 확인해 주세요.
                </p>

                <button className="btn" onClick={() => setRevealed(true)}>
                  합격 확인
                </button>

                <p className="hint">※ 화면은 데모(연출)용입니다.</p>
              </>
            ) : (
              <div className="result">
                <div className="stamp" aria-hidden="true">PASS</div>
                <h1 className="passTitle">합격입니다</h1>
                <p className="passSub">
                  축하드립니다. <br />
                  KIA 경력직 채용 전형에 최종 합격하셨습니다.
                </p>

                <div className="resultBox">
                  <div className="row">
                    <span className="k">지원분야</span>
                    <span className="v">생산/품질 (경력)</span>
                  </div>
                  <div className="row">
                    <span className="k">결과</span>
                    <span className="v strong">최종 합격</span>
                  </div>
                  <div className="row">
                    <span className="k">안내</span>
                    <span className="v">추후 절차는 이메일/문자 안내 예정</span>
                  </div>
                </div>

                <div className="actions">
                  <button className="btnGhost" onClick={() => setRevealed(false)}>
                    다시 보기
                  </button>
                  <button className="btn" onClick={() => alert("축하합니다! (데모)")}>
                    확인
                  </button>
                </div>
              </div>
            )}
          </div>
        </section>
      </main>

      <style>{`
        :root{
          --dark0:#050711;
          --dark1:#0b0f19;
          --line:rgba(255,255,255,.10);
          --text:#e7eaf0;
          --muted:rgba(231,234,240,.70);
          --kia:#ff2b2b;
          --lightBg:#f6f7fb;
          --lightCard:#ffffff;
          --lightText:#10131a;
          --lightMuted:rgba(16,19,26,.65);
        }

        *{box-sizing:border-box}
        html,body{height:100%}
        body{margin:0;font-family:system-ui,-apple-system,"Noto Sans KR",sans-serif}

        .page{
          min-height:100vh;
          display:flex;
          align-items:center;
          justify-content:center;
          background: radial-gradient(1200px 700px at 20% 10%, #151a2d, var(--dark0));
          color:var(--text);
          position:relative;
          overflow:hidden;
        }

        /* Light overlay that fades in */
        .lightLayer{
          position:absolute; inset:0;
          background: radial-gradient(1200px 700px at 20% 10%, #ffffff, var(--lightBg));
          opacity:0;
          transition: opacity 900ms cubic-bezier(.2,.9,.2,1);
        }
        .revealed .lightLayer{ opacity:1; }

        .wrap{
          width:min(980px, 92vw);
          position:relative;
          z-index:1;
          padding:28px 0;
        }

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
            border-color 900ms cubic-bezier(.2,.9,.2,1);
        }

        .revealed .card{
          background: rgba(255,255,255,.92);
          border-color: rgba(16,19,26,.10);
          color: var(--lightText);
          box-shadow: 0 26px 70px rgba(0,0,0,.18);
        }

        .cardZoom{
          transform: scale(1.08);
        }

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
          background: rgba(255,43,43,.18);
          border:1px solid rgba(255,43,43,.35);
          color: var(--kia);
          font-weight:800;
          letter-spacing:.5px;
        }
        .brandTitle{font-weight:800; font-size:16px; line-height:1.2}
        .brandSub{font-size:12.5px; color:var(--muted); margin-top:2px}
        .revealed .brandSub{ color: var(--lightMuted); }

        .meta{display:flex; flex-direction:column; gap:8px; align-items:flex-end}
        .metaRow{display:flex; gap:8px; align-items:center; font-size:12.5px; color:var(--muted)}
        .revealed .metaRow{ color: var(--lightMuted); }
        .dot{width:7px;height:7px;border-radius:50%; background:rgba(255,255,255,.35)}
        .revealed .dot{ background: rgba(16,19,26,.25); }

        .pill{
          font-size:12px;
          padding:6px 10px;
          border-radius:999px;
          border:1px solid rgba(255,255,255,.14);
          background: rgba(255,255,255,.04);
          color: rgba(231,234,240,.85);
        }
        .revealed .pill{
          border:1px solid rgba(16,19,26,.10);
          background: rgba(16,19,26,.03);
          color: rgba(16,19,26,.80);
        }

        .divider{
          height:1px;
          background: rgba(255,255,255,.10);
        }
        .revealed .divider{ background: rgba(16,19,26,.10); }

        .content{
          padding:22px 18px 20px 18px;
        }

        .h1{
          margin:0 0 10px 0;
          font-size:22px;
          letter-spacing:-.2px;
        }

        .p{
          margin:0 0 18px 0;
          color:var(--muted);
          line-height:1.6;
        }
        .revealed .p{ color: var(--lightMuted); }

        .btn{
          width:100%;
          border:0;
          padding:14px 14px;
          border-radius:14px;
          background: var(--kia);
          color:#fff;
          font-weight:800;
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
          font-weight:800;
          font-size:15px;
          cursor:pointer;
        }
        .revealed .btnGhost{
          border:1px solid rgba(16,19,26,.12);
          color: var(--lightText);
        }

        .hint{
          margin:12px 0 0 0;
          font-size:12px;
          color: rgba(231,234,240,.55);
        }
        .revealed .hint{ color: rgba(16,19,26,.50); }

        /* Result screen */
        .result{
          position:relative;
          padding-top:6px;
          animation: pop 520ms cubic-bezier(.2,.9,.2,1) both;
        }

        .stamp{
          position:absolute;
          right:0;
          top:-10px;
          font-weight:900;
          letter-spacing:2px;
          padding:10px 12px;
          border-radius:12px;
          border:2px solid rgba(255,43,43,.45);
          color: var(--kia);
          background: rgba(255,43,43,.06);
          transform: rotate(8deg);
        }

        .passTitle{
          margin:0 0 8px 0;
          font-size:34px;
          letter-spacing:-.8px;
          font-weight:900;
        }

        .passSub{
          margin:0 0 16px 0;
          color: var(--lightMuted);
          line-height:1.6;
        }

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
        .strong{font-weight:900; color: #0a0a0a;}

        .actions{display:flex; gap:10px;}
        .actions > button{flex:1}

        @keyframes pop{
          from{ transform: translateY(10px); opacity:0; }
          to{ transform: translateY(0); opacity:1; }
        }

        @media (prefers-reduced-motion: reduce){
          .lightLayer, .card{ transition:none !important; }
          .result{ animation:none !important; }
        }
      `}</style>
    </div>
  );
}
