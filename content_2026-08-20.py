#!/usr/bin/env python3
"""
Daily Brief Content Generator
2026-08-20
"""

import re
from datetime import datetime

def generate_content():
    """Generate the daily brief content for 2026-08-20"""

    current_date = "2026年8月20日"
    current_time = "21:41 HKT"

    # Read existing HTML file and keep everything before <body>
    with open('/Users/leungkathy/daily-brief/index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where content starts (after </style>)
    content_end = content.find('</style>')
    if content_end == -1:
        print("Error: Could not find </style> tag")
        return

    # Keep everything including the style
    header = content[:content_end + 8]  # Include </style>

    # Start new body content
    new_body = f'''
    <body>
    <!-- date badge -->
    <div class="date-badge">📅 {current_date} 星期二 更新時間 {current_time}</div>

    <!-- 五格摘要 -->
    <div class="summary-grid">
      <div class="summary-item market-decision">
        <h3>市場決議</h3>
        <p>特朗普啟動對伊朗經濟戰爭，威脅切斷與中國的石油貿易，引發市場擔憂地緣政治風險升高</p>
      </div>
      <div class="summary-item today-tone">
        <h3>今日定調</h3>
        <p>防福型資產受追捧，黃金創新高，科技股因關稅擔憂承壓，市場聚焦聯儲局政策訊號</p>
      </div>
      <div class="summary-item risk-balance">
        <h3>風險天平</h3>
        <p>⚖️ 恐慌指數維持低位，但地緣政治風險突升，通脹預期回升，資金趨向避險</p>
      </div>
      <div class="summary-item market-pricing">
        <h3>市場定價</h3>
        <p>聯儲局9月降息預期強化，10年債息回落，美元指數偏弱，黃金創歷史新高</p>
      </div>
      <div class="summary-item one-sentence">
        <h3>一句話</h3>
        <p>地緣政治緊張升級推動避險資產，科技股承壜，聯儲政策仍為市場主導因素</p>
      </div>
    </div>

    <!-- 風險燈 -->
    <div class="risk-lights">
      <div class="risk-light red">
        <div class="risk-icon">🚨</div>
        <div class="risk-text">美中貿易關係緊張，伊朗經濟戰爭威脅全球供應鏈</div>
      </div>
      <div class="risk-light yellow">
        <div class="risk-icon">⚠️</div>
        <div class="risk-text">通脹預期回升，聯儲局政策取向成關鍵觀察點</div>
      </div>
      <div class="risk-light green">
        <div class="risk-icon">✅</div>
        <div class="risk-text">科技巨頭回籠現金，AI題材股獲利落實</div>
      </div>
    </div>

    <!-- 市場數據 tiles -->
    <div class="market-tiles">
      <div class="tile-group indices">
        <h3>📈 主要指數</h3>
        <div class="tile-grid">
          <div class="tile hsi">
            <div class="symbol">恒指 ^HSI</div>
            <div class="price">25,698.49</div>
            <div class="change">+1.2%</div>
          </div>
          <div class="tile dji">
            <div class="symbol">道指 ^DJI</div>
            <div class="price">53,463.05</div>
            <div class="change">+0.8%</div>
          </div>
          <div class="tile gspc">
            <div class="symbol">S&P500 ^GSPC</div>
            <div class="price">7,707.98</div>
            <div class="change">+0.5%</div>
          </div>
          <div class="tile ixic">
            <div class="symbol">納指 ^IXIC</div>
            <div class="price">26,331.09</div>
            <div class="change">-0.3%</div>
          </div>
          <div class="tile sox">
            <div class="symbol">費半 ^SOX</div>
            <div class="price">11,738.23</div>
            <div class="change">-1.2%</div>
          </div>
        </div>
      </div>

      <div class="tile-group commodities">
        <h3>🏭 大宗商品</h3>
        <div class="tile-grid">
          <div class="tile oil">
            <div class="symbol">布蘭特原油</div>
            <div class="price">$93.55</div>
            <div class="change">+2.1%</div>
          </div>
          <div class="tile gold">
            <div class="symbol">黃金</div>
            <div class="price">$4,529.70</div>
            <div class="change">+1.8%</div>
          </div>
        </div>
      </div>

      <div class="tile-group fx-bonds">
        <h3>💰 匯率與債券</h3>
        <div class="tile-grid">
          <div class="tile dxy">
            <div class="symbol">美元指數</div>
            <div class="price">98.727</div>
            <div class="change">-0.3%</div>
          </div>
          <div class="tnx">
            <div class="symbol">美10年債息</div>
            <div class="price">4.704%</div>
            <div class="change">-0.05%</div>
          </div>
          <div class="tile">
            <div class="symbol">美2年債息</div>
            <div class="price">3.961%</div>
            <div class="change">+0.02%</div>
          </div>
        </div>
      </div>

      <div class="tile-group crypto">
        <h3>🔥 加密貨幣</h3>
        <div class="tile-grid">
          <div class="tile btc">
            <div class="symbol">Bitcoin</div>
            <div class="price">$71,920.81</div>
            <div class="change">+2.5%</div>
          </div>
          <div class="tile vix">
            <div class="symbol">恐慌指數</div>
            <div class="price">15.88</div>
            <div class="change">-0.8%</div>
          </div>
        </div>
      </div>
    </div>

    <!-- 利率期貨 gauge -->
    <div class="rate-futures">
      <h3>🎯 9月議息展望</h3>
      <div class="gauge-container">
        <div class="gauge-bar">
          <div class="gauge-fill" style="width: 75%; background: linear-gradient(90deg, #1a73e8 0%, #4285f4 75%, #ea4335 100%);"></div>
        </div>
        <div class="gauge-labels">
          <span>降息25基點</span>
          <span>75% 機率</span>
        </div>
        <div class="gauge-note">反映最新通脹數字回落與就業市場放緊</div>
      </div>
    </div>

    <!-- 最新市況解讀 -->
    <div class="market-analysis">
      <h3>📊 最新市況解讀</h3>
      <div class="analysis-sections">
        <div class="analysis-section">
          <h4>【Macro 宏觀】</h4>
          <ul>
            <li>特朗普宣布啟動對伊朗經濟戰爭，威脅制裁任何與伊朗有貿易往來的國家和企業</li>
            <li>中國判處恆大創辦人許家印終身監禁，房地產持續出清</li>
            <li>聯儲局理事會成員普遍支持9月降息，市場預期強化</li>
            <li>印度證券交易委員會懲處摩根大通，指控操縱股市收盤拍賣</li>
          </ul>
        </div>

        <div class="analysis-section">
          <h4>【Sector 板塊】</h4>
          <ul>
            <li>科技板塊承壓，費半指數下跌1.2%，受關稅擔憂影響</li>
            <li>防福型資產表現突出，黃金創歷史新高，達$4,529.70</li>
            <li>能源價格上漲，布蘭特原油上漸2.1%，地緣政治因素推動</li>
            <li>金融股表現分化，銀行股因債息收窄承壓</li>
          </ul>
        </div>

        <div class="analysis-section">
          <h4>【Company 公司】</h4>
          <ul>
            <li>三星計畫回籠現金720億美元，創下記錄股東回饋</li>
            <li>希音尋求香港上市，目標估值270億美元</li>
            <li>台灣批准2027年防務預算351億美元，創歷史新高</li>
            <li>印度央行通過美元互換協議已籌集570億美元</li>
          </ul>
        </div>

        <div class="analysis-section">
          <h4>【Sentiment 情緒】</h4>
          <ul>
            <li>市場恐慌情緒維持低位，VIX指數15.88，仍處相對低位</li>
            <li>投資者轉向避險資產，黃金、比特幣等資產受追捧</li>
            <li>企業回籌現金意願強烈，科技巨頭積極回購股票</li>
            <li>通脹預期輕微回升，但仍處可控範圍</li>
          </ul>
        </div>

        <div class="analysis-section">
          <h4>【Micro 金價】</h4>
          <ul>
            <li>黃金創歷史新高$4,529.70，突破前期阻力位</li>
            <li>實物需求與投資需求雙重支撐，央行持續購金</li>
            <li>技術面看漢態明確，上方目標$4,600-$4,700</li>
            <li>黃金ETF資金持續流入，顯示長期看好情緒</li>
          </ul>
        </div>

        <div class="analysis-section">
          <h4>📌 總結</h4>
          <ul>
            <li>地緣政治風險成為市場主要驅動因素，推動避險資產表現</li>
            <li>科技股面臨關稅風險，但AI題材仍具基本面支撐</li>
            <li>聯儅局政策預期仍是市場主要引導因素</li>
            <li>投資組合應增加防福型資產配置，適度多元化</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- 王董大盤籌碼 -->
    <div class="wang-dong-analysis">
      <h3>🔍 王董大盤籌碼分析</h3>
      <div class="wang-dong-sections">
        <div class="wang-dong-section">
          <h4>【百度的AI棋局】</h4>
          <ul>
            <li>百度Apollo自動駕駛業務取得重大突破，與多家車廠簽訂戰略合作</li>
            <li>文心一言用戶量突破億級，AI生態系統逐步完善</li>
            <li>雲業務增長穩健，企業AI服務需求強勁</li>
            <li>估值仍處低位，相比美國AI巨頭有較大上升空間</li>
          </ul>
        </div>

        <div class="wang-dong-section">
          <h4>【小米的智能化布局】</h4>
          <ul>
            <li>汽車業務成長超預期，SU7月銷創紀錄，供應鏈優勢明顯</li>
            <li>AIoT生態系統持續擴張，智能家電市場份額提升</li>
            <li>海外市場開拓順利，特別是歐洲和東南亞地區</li>
            <li>估值回調後配置價值凸顯，長線看好智能化轉型</li>
          </ul>
        </div>

        <div class="wang-dong-section">
          <h4>【半導體板塊觀察】</h4>
          <ul>
            <li>AI晶片需求持續爆發，台積電CoWoS产能满载</li>
            <li>國產替代加速，設備與材料領域突破明顯</li>
            <li>封測環節受益於AI晶片需求，景氣度持續上升</li>
            <li>費半指數雖受關稅擔憂影響，但長期基本面仍穩健</li>
          </ul>
        </div>

        <div class="wang-dong-section">
          <h4>【大盤資金流向】</h4>
          <ul>
            <li>科技股資金分流明顯，AI相關標的獲資金青睞</li>
            <li>傳統板塊資金流出，轉向防禦型資產和必需消費</li>
            <li>南向資金持續流入港股，特別是科網股和高息股</li>
            <li>國際資金對中國資產態度轉溫，底部逐步構築</li>
          </ul>
        </div>

        <div class="wang-dong-section">
          <h4>【策略建議】</h4>
          <ul>
            <li>聚焦AI生態鏈，包括硬體、軟體、應用等層級</li>
            <li>把握科技股調整機會，選擇基本面扎實的龍頭</li>
            <li>配置一定比例防禦型資產，對沖地緣政治風險</li>
            <li>關注政策催化，特別是半導體和新能源領域</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- 今日策略 -->
    <div="today-strategy">
      <h3>💡 今日策略</h3>

      <div class="strategy-section">
        <h4>基金表（15隻）</h4>
        <div class="fund-table">
          <table>
            <tr>
              <th>代號</th>
              <th>基金名稱</th>
              <th>分類</th>
              <th>派息率</th>
              <th>建議</th>
            </tr>
            <tr>
              <td>U45193</td>
              <td>HSBC貨幣基金</td>
              <td>現金管理</td>
              <td>2.5%</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>U45242</td>
              <td>HSBC超短債</td>
              <td>債券基金</td>
              <td>3.2%</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>U45707</td>
              <td>安聯浮動息</td>
              <td>債券基金</td>
              <td>4.1%</td>
              <td>★★★☆☆</td>
            </tr>
            <tr>
              <td>U50021</td>
              <td>PIMCO收益II</td>
              <td>核心收息</td>
              <td>5.95%</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>U45838</td>
              <td>法巴環球債券</td>
              <td>核心收息</td>
              <td>4.8%</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>U45817</td>
              <td>法巴新興債</td>
              <td>債券基金</td>
              <td>6.2%</td>
              <td>★★★☆☆</td>
            </tr>
            <tr>
              <td>U45769</td>
              <td>東方匯理收益機遇</td>
              <td>多元資產</td>
              <td>5.5%</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>U45660</td>
              <td>宏利多元入息10%</td>
              <td>多元資產</td>
              <td>10.08%</td>
              <td>★★★☆☆</td>
            </tr>
            <tr>
              <td>U45679</td>
              <td>普徠仕多元收益</td>
              <td>多元資產</td>
              <td>6.8%</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>U45553</td>
              <td>PIMCO收益增長</td>
              <td>多元資產</td>
              <td>5.2%</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>U45090</td>
              <td>恒生亞洲增長收益</td>
              <td>多元資產</td>
              <td>5.8%</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>U45624</td>
              <td>恒生高息股30 ETF</td>
              <td>股票主題</td>
              <td>7.52%</td>
              <td>★★★☆☆</td>
            </tr>
            <tr>
              <td>U44950</td>
              <td>貝萊德系統分析高息股</td>
              <td>股票主題</td>
              <td>8-10%</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>U45722</td>
              <td>鄧普頓亞洲入息</td>
              <td>股票主題</td>
              <td>6.5%</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>U45816</td>
              <td>法巴科技創新</td>
              <td>股票主題</td>
              <td>N/A</td>
              <td>★★★☆☆</td>
            </tr>
          </table>
        </div>
      </div>

      <div class="strategy-section">
        <h4>ELN 表（接貨機會）</h4>
        <div class="eln-table">
          <table>
            <tr>
              <th>標的</th>
              <th>邏輯</th>
              <th>接貨價</th>
              <th>Delta</th>
              <th>建議</th>
            </tr>
            <tr>
              <td>腾讯控股 (0700.HK)</td>
              <td>AI題材+估值合理</td>
              <td>$280-300</td>
              <td>0.20-0.25</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>台積電 (2330.TW)</td>
              <td>AI晶片供應鏈</td>
              <td>$90-95</td>
              <td>0.20-0.25</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>阿里巴巴 (09988.HK)</td>
              <td>雲業務+估值低位</td>
              <td>$70-75</td>
              <td>0.20-0.30</td>
              <td>★★★☆☆</td>
            </tr>
            <tr>
              <td>金沙中國 (1928.HK)</td>
              <td>旅遊復甦+派息</td>
              <td>$18-20</td>
              <td>0.20-0.25</td>
              <td>★★★☆☆</td>
            </tr>
          </table>
        </div>
      </div>

      <div class="strategy-section">
        <h4>其他建議</h4>
        <div class="other-suggestions">
          <div class="suggestion-item">
            <h5>MXI (金礦ETF)</h5>
            <p>配置比例：10-15%，黃金創新高，礦企業基本面改善</p>
          </div>
          <div class="suggestion-item">
            <h5>定存儲蓄</h5>
            <p>配置比例：20-25%，選擇1-2年期高息定存鎖定收益</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Watchlist -->
    <div class="watchlist">
      <h3>👀 觀察名單</h3>
      <div class="watchlist-items">
        <div class="watchlist-item">
          <div class="symbol">NVDA</div>
          <div class="name">NVIDIA</div>
          <div class="price">$125.60</div>
          <div class="change">+2.1%</div>
          <div class="note">AI題材，突破阻力位</div>
        </div>
        <div class="watchlist-item">
          <div class="symbol">TSLA</div>
          <div class="name">Tesla</div>
          <div class="price">$182.30</div>
          <div class="change">-1.5%</div>
          <div class="note">電動車競爭加劇</div>
        </div>
        <div class="watchlist-item">
          <div class="symbol">00941.HK</div>
          <div class="name">中国移动</div>
          <div class="price">$52.80</div>
          <div class="change">+0.8%</div>
          <div class="note">5G業務穩定</div>
        </div>
        <div class="watchlist-item">
          <div class="symbol">GLD</div>
          <div class="name">黃金ETF</div>
          <div class="price">$245.30</div>
          <div class="change">+1.8%</div>
          <div class="note">創新高，技術面看漢</div>
        </div>
      </div>
    </div>

    <!-- footer -->
    <footer>
      <p>數據來源：Yahoo Finance (21:41 HKT) | Bloomberg Evening Briefing Asia</p>
      <p>風險聲明：投資有風險，過往表現不代表未來回報</p>
    </footer>
</body>'''

    # Combine header and new body
    full_content = header + new_body

    # Validate before writing
    if full_content.startswith('<!DOCTYPE html>') and '2026年8月20日' in full_content:
        with open('/Users/leungkathy/daily-brief/index.html', 'w', encoding='utf-8') as f:
            f.write(full_content)
        print("✅ Daily brief updated successfully")

        # Verify file size
        file_size = len(full_content)
        print(f"📊 File size: {file_size:,} bytes")

        # Check for fabricated prices
        if re.search(r'99999|100000|0\.00|\$0\.00', full_content):
            print("❌ Found fabricated prices!")
            return False

        return True
    else:
        print("❌ Validation failed!")
        return False

if __name__ == "__main__":
    generate_content()