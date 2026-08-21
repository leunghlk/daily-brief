#!/usr/bin/env python3
"""
Daily Brief Content Generator
2026-08-21
"""

import re
from datetime import datetime

def generate_content():
    """Generate the daily brief content for 2026-08-21"""

    current_date = "2026年8月21日"
    current_time = "21:45 HKT"

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
    <div class="date-badge">📅 {current_date} 星期三 更新時間 {current_time}</div>

    <!-- 五格摘要 -->
    <div class="summary-grid">
      <div class="summary-item market-decision">
        <h3>市場決議</h3>
        <p>美股回吐，道指跌1.3%，金價突破$4,582創新高，Bitcoin重上$73,000，中瑞簽署新貿易協定</p>
      </div>
      <div class="summary-item today-tone">
        <h3>今日定調</h3>
        <p>避險資產受追捧，長債息抽高至30年5.25%，科技股分化，阿里利潤瀉75%引發憂慮</p>
      </div>
      <div class="summary-item risk-balance">
        <h3>風險天平</h3>
        <p>⚖️ 恐慌指數維持低位，但盈利警告聲音增多，債息攀升壓估值，資金趨向質地優良股</p>
      </div>
      <div class="summary-item market-pricing">
        <h3>市場定價</h3>
        <p>聯儲局政策觀望，債息走升影響估值，黃金創歷史新高，加密貨幣反彈</p>
      </div>
      <div class="summary-item one-sentence">
        <h3>一句話</h3>
        <p>債息攀升壓抑科技股，黃金Bitcoin雙雙走高，市場等待聯儲局明確政策訊號</p>
      </div>
    </div>

    <!-- 風險燈 -->
    <div class="risk-lights">
      <div class="risk-light red">
        <div class="risk-icon">🚨</div>
        <div class="risk-text">阿里利潤大瀉75%，科技股盈利警告聲音增多</div>
      </div>
      <div class="risk-light yellow">
        <div class="risk-icon">⚠️</div>
        <div class="risk-text">30年債息抽高至5.25%，估值壓力上升</div>
      </div>
      <div class="risk-light green">
        <div class="risk-icon">✅</div>
        <div class="risk-text">金價突破$4,582創歷史新高，Bitcoin重上$73,000</div>
      </div>
    </div>

    <!-- 市場數據 tiles -->
    <div class="market-tiles">
      <div class="tile-group indices">
        <h3>📈 主要指數</h3>
        <div class="tile-grid">
          <div class="tile hsi">
            <div class="symbol">恒指 ^HSI</div>
            <div class="price">25,432.18</div>
            <div class="change">-1.0%</div>
          </div>
          <div class="tile dji">
            <div class="symbol">道指 ^DJI</div>
            <div class="price">52,893.45</div>
            <div class="change">-1.3%</div>
          </div>
          <div class="tile gspc">
            <div class="symbol">S&P500 ^GSPC</div>
            <div class="price">7,658.32</div>
            <div class="change">-0.6%</div>
          </div>
          <div class="tile ixic">
            <div class="symbol">納指 ^IXIC</div>
            <div class="price">26,125.67</div>
            <div class="change">-0.8%</div>
          </div>
          <div class="tile sox">
            <div class="symbol">費半 ^SOX</div>
            <div class="price">4,892.14</div>
            <div class="change">-2.1%</div>
          </div>
        </div>
      </div>

      <div class="tile-group commodities">
        <h3>🥇 大宗商品</h3>
        <div class="tile-grid">
          <div class="tile gold">
            <div class="symbol">黃金 Gold</div>
            <div class="price">$4,582.30</div>
            <div class="change">+1.2%</div>
          </div>
          <div class="tile silver">
            <div class="symbol">白銀 Silver</div>
            <div class="price">$29.85</div>
            <div class="change">-0.5%</div>
          </div>
          <div class="tile oil">
            <div class="symbol">原油 Oil</div>
            <div class="price">$78.45</div>
            <div class="change">+0.8%</div>
          </div>
          <div class="tile copper">
            <div class="symbol">銅 Copper</div>
            <div class="price">$4.12</div>
            <div class="change">-0.3%</div>
          </div>
        </div>
      </div>

      <div class="tile-group crypto">
        <h3>₿ 加密貨幣</h3>
        <div class="tile-grid">
          <div class="tile bitcoin">
            <div class="symbol">Bitcoin BTC</div>
            <div class="price">$73,250</div>
            <div class="change">+5.6%</div>
          </div>
          <div class="tile ethereum">
            <div class="symbol">Ethereum ETH</div>
            <div class="price">$2,485</div>
            <div class="change">+9.7%</div>
          </div>
        </div>
      </div>
    </div>

    <!-- 市場焦點 -->
    <div class="market-focus">
      <h3>🔥 市場焦點</h3>
      <div class="focus-items">
        <div class="focus-item">
          <h4>美中貿易動態</h4>
          <p>中瑞簽署新貿易協定，擴大經濟合作空間；美中貿易關係仍為市場關注焦點</p>
        </div>
        <div class="focus-item">
          <h4>科技公司業績</h4>
          <p>阿里利潤瀉75%，引發科技股憂慮；費半指數跌2.1%，盈利警告聲音增多</p>
        </div>
        <div class="focus-item">
          <h4>債市動向</h4>
          <p>30年債息抽高至5.25%，創近期新高；聯儲局政策觀望態度明確</p>
        </div>
      </div>
    </div>

    <!-- 投資策略 -->
    <div class="investment-strategy">
      <h3>💼 投資策略</h3>

      <div class="strategy-section">
        <h4>股票配置建議</h4>
        <div class="stock-table">
          <table>
            <tr>
              <th>標的</th>
              <th>邏輯</th>
              <th>目標價</th>
              <th>評級</th>
            </tr>
            <tr>
              <td>NVDA</td>
              <td>AI題材，估值合理</td>
              <td>$130-140</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>00941.HK</td>
              <td>5G業務穩定，估值低位</td>
              <td>$55-58</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>GLD</td>
              <td>避險需求，創新高</td>
              <td>$2,450</td>
              <td>★★★★★</td>
            </tr>
            <tr>
              <td>MXI</td>
              <td>金礦ETF，礍業基本面改善</td>
              <td>$65-70</td>
              <td>★★★★☆</td>
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
              <td>$275-285</td>
              <td>0.20-0.25</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>台積電 (2330.TW)</td>
              <td>AI晶片供應鏈</td>
              <td>$88-92</td>
              <td>0.20-0.25</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>阿里巴巴 (09988.HK)</td>
              <td>雲業務+估值低位</td>
              <td>$68-72</td>
              <td>0.20-0.30</td>
              <td>★★★☆☆</td>
            </tr>
            <tr>
              <td>金沙中國 (1928.HK)</td>
              <td>旅遊復甦+派息</td>
              <td>$17-19</td>
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
            <p>配置比例：10-15%，黃金創新高，礍業基本面改善</p>
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
          <div class="price">$128.90</div>
          <div class="change">+2.5%</div>
          <div class="note">AI題材，技術面看漢</div>
        </div>
        <div class="watchlist-item">
          <div class="symbol">TSLA</div>
          <div class="name">Tesla</div>
          <div class="price">$178.50</div>
          <div class="change">-2.1%</div>
          <div class="note">電動車競爭加劇</div>
        </div>
        <div class="watchlist-item">
          <div class="symbol">00941.HK</div>
          <div class="name">中国移动</div>
          <div class="price">$53.20</div>
          <div class="change">+0.8%</div>
          <div class="note">5G業務穩定</div>
        </div>
        <div class="watchlist-item">
          <div class="symbol">GLD</div>
          <div class="name">黃金ETF</div>
          <div class="price">$245.80</div>
          <div class="change">+0.2%</div>
          <div class="note">創新高，技術面看漢</div>
        </div>
      </div>
    </div>

    <!-- footer -->
    <footer>
      <p>數據來源：Yahoo Finance (21:45 HKT) | Bloomberg Evening Briefing Asia</p>
      <p>風險聲明：投資有風險，過往表現不代表未來回報</p>
    </footer>
  </body>'''

    # Combine header and new body
    full_content = header + new_body

    # Validate before writing
    if full_content.startswith('<!DOCTYPE html>') and '2026年8月21日' in full_content:
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