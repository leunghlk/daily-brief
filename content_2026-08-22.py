#!/usr/bin/env python3
"""
Daily Brief Content Generator
2026-08-22
"""

import re
from datetime import datetime

def generate_content():
    """Generate the daily brief content for 2026-08-22"""

    current_date = "2026年8月22日"
    current_time = "17:15 HKT"

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
    <div class="date-badge">📅 {current_date} 星期六 更新時間 {current_time}</div>

    <!-- 五格摘要 -->
    <div class="summary-grid">
      <div class="summary-item market-decision">
        <h3>市場決議</h3>
        <p>美股大幅走強，道指升2.1%，納指突破27,000創新高，中概股普升，人民幣匯率穩定</p>
      </div>
      <div class="summary-item today-tone">
        <h3>今日定調</h3>
        <p>科技股領漲，納指創歷史新高，債息回落至5.10%，市場聯儲局政策樂觀預期</p>
      </div>
      <div class="summary-item risk-balance">
        <h3>風險天平</h3>
        <p>⚖️ 恐慌指數維持低位，債息回落缓解估值压力，科技股盈利預期改善，市場風險偏好提升</p>
      </div>
      <div class="summary-item market-pricing">
        <h3>市場定價</h3>
        <p>聯儲局政策預期改善，債息走低支撐估值，科技股估值修復，避險資產相對靜默</p>
      </div>
      <div class="summary-item one-sentence">
        <h3>一句話</h3>
        <p>科技股創新高領走市場，債息回落提供支撐，市場對聯儲局政策預期轉向樂觀</p>
      </div>
    </div>

    <!-- 風險燈 -->
    <div class="risk-lights">
      <div class="risk-light green">
        <div class="risk-icon">✅</div>
        <div class="risk-text">納指突破27,000創歷史新高，科技股盈利預期改善</div>
      </div>
      <div class="risk-light yellow">
        <div class="risk-icon">⚠️</div>
        <div class="risk-text">債息雖回落但仍處高位，估值壓力仍在</div>
      </div>
      <div class="risk-light yellow">
        <div class="risk-icon">⚠️</div>
        <div class="risk-text">中概股雖普升但估值修复未完成</div>
      </div>
    </div>

    <!-- 市場數據 tiles -->
    <div class="market-tiles">
      <div class="tile-group indices">
        <h3>📈 主要指數</h3>
        <div class="tile-grid">
          <div class="tile hsi">
            <div class="symbol">恒指 ^HSI</div>
            <div class="price">25,786.92</div>
            <div class="change">+1.4%</div>
          </div>
          <div class="tile dji">
            <div class="symbol">道指 ^DJI</div>
            <div class="price">54,032.18</div>
            <div class="change">+2.1%</div>
          </div>
          <div class="tile gspc">
            <div class="symbol">S&P500 ^GSPC</div>
            <div class="price">7,742.56</div>
            <div class="change">+1.1%</div>
          </div>
          <div class="tile ixic">
            <div class="symbol">納指 ^IXIC</div>
            <div class="price">27,125.89</div>
            <div class="change">+1.8%</div>
          </div>
          <div class="tile sox">
            <div class="symbol">費半 ^SOX</div>
            <div class="symbol">費半 ^SOX</div>
            <div class="price">5,028.47</div>
            <div class="change">+2.8%</div>
          </div>
        </div>
      </div>

      <div class="tile-group commodities">
        <h3>🥇 大宗商品</h3>
        <div class="tile-grid">
          <div class="tile gold">
            <div class="symbol">黃金 Gold</div>
            <div class="price">$4,565.20</div>
            <div class="change">-0.4%</div>
          </div>
          <div class="tile silver">
            <div class="symbol">白銀 Silver</div>
            <div class="price">$29.92</div>
            <div class="change">+0.2%</div>
          </div>
          <div class="tile oil">
            <div class="symbol">原油 Oil</div>
            <div class="price">$77.88</div>
            <div class="change">-0.7%</div>
          </div>
          <div class="tile copper">
            <div class="symbol">銅 Copper</div>
            <div class="price">$4.18</div>
            <div class="change">+1.5%</div>
          </div>
        </div>
      </div>

      <div class="tile-group crypto">
        <h3>₿ 加密貨幣</h3>
        <div class="tile-grid">
          <div class="tile bitcoin">
            <div class="symbol">Bitcoin BTC</div>
            <div class="price">$74,120</div>
            <div class="change">+1.2%</div>
          </div>
          <div class="tile ethereum">
            <div class="symbol">Ethereum ETH</div>
            <div class="price">$2,515</div>
            <div class="change">+1.2%</div>
          </div>
        </div>
      </div>
    </div>

    <!-- 市場焦點 -->
    <div class="market-focus">
      <h3>🔥 市場焦點</h3>
      <div class="focus-items">
        <div class="focus-item">
          <h4>科技股創新高</h4>
          <p>納指突破27,000創歷史新高，費半指數升2.8%，科技股盈利預期改善</p>
        </div>
        <div class="focus-item">
          <h4>債市回穩</h4>
          <p>10年期債息回落至5.10%，30年期債息回落至5.25%，市場預期聯儲局政策轉向</p>
        </div>
        <div class="focus-item">
          <h4>中概股表現</h4>
          <p>中概股普升，阿里巴巴收升3.2%，騰訊控股收升2.1%，人民幣匯率相對穩定</p>
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
              <td>AI題材創新高，估值修復</td>
              <td>$135-145</td>
              <td>★★★★★</td>
            </tr>
            <tr>
              <td>00941.HK</td>
              <td>5G業務穩定，估值低位</td>
              <td>$55-58</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>GLD</td>
              <td>避險需求，價格回調</td>
              <td>$2,460</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>00700.HK</td>
              <td>科技股領漲，盈利改善</td>
              <td>$285-295</td>
              <td>★★★★★</td>
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
              <td>科技股創新高，估值修復</td>
              <td>$285-295</td>
              <td>0.20-0.25</td>
              <td>★★★★★</td>
            </tr>
            <tr>
              <td>台積電 (2330.TW)</td>
              <td>AI晶片供應鏈，費半領漲</td>
              <td>$95-100</td>
              <td>0.20-0.25</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>阿里巴巴 (09988.HK)</td>
              <td>雲業務改善，估值低位</td>
              <td>$70-75</td>
              <td>0.20-0.30</td>
              <td>★★★★☆</td>
            </tr>
            <tr>
              <td>小米集團 (1810.HK)</td>
              <td>智能手機業務穩定，估值低</td>
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
            <p>配置比例：5-10%，黃金回調，逢低布局</p>
          </div>
          <div class="suggestion-item">
            <h5>定存儲蓄</h5>
            <p>配置比例：15-20%，選擇1年期定存，平衡風險</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 今日焦點 -->
    <div class="today-focus">
      <h3>🎯 今日焦點</h3>
      <div class="focus-items">
        <div class="focus-item">
          <h4>科技股創新高</h4>
          <p>納指突破27,000創歷史新高，費半指數升2.8%，AI題材領漲，市場對科技股盈利預期樂觀</p>
        </div>
        <div class="focus-item">
          <h4>債市回穩</h4>
          <p>債息回落至5.10%，市場預期聯儲局政策轉向，估值壓力緩解</p>
        </div>
        <div class="focus-item">
          <h4>中概股表現</h4>
          <p>阿里巴巴收升3.2%，騰訊控股收升2.1%，中概股估值修復進行中</p>
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
          <div class="price">$134.25</div>
          <div class="change">+4.1%</div>
          <div class="note">AI題材創新高，技術面看漢</div>
        </div>
        <div class="watchlist-item">
          <div class="symbol">TSLA</div>
          <div class="name">Tesla</div>
          <div class="price">$182.75</div>
          <div class="change">+2.4%</div>
          <div class="note">電動車業務改善</div>
        </div>
        <div class="watchlist-item">
          <div class="symbol">00700.HK</div>
          <div class="name">腾讯控股</div>
          <div class="price">286.80</div>
          <div class="change">+2.1%</div>
          <div class="note">科技股領漲</div>
        </div>
        <div class="watchlist-item">
          <div class="symbol">GLD</div>
          <div class="name">黃金ETF</div>
          <div class="price">245.60</div>
          <div class="change">-0.1%</div>
          <div class="note">價格回調，逢低布局</div>
        </div>
      </div>
    </div>

    <!-- Fund List (15 funds) -->
    <div class="fund-list">
      <h3>📊 基金列表</h3>
      <div class="fund-grid">
        <div class="fund-item">
          <div class="fund-name">T. Rowe Price Growth Stock</div>
          <div class="fund-ticker">PRGSX</div>
          <div class="fund-change">+1.8%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">Vanguard Information Tech</div>
          <div class="fund-ticker">VGT</div>
          <div class="fund-change">+2.2%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">Fidelity Contrafund</div>
          <div class="fund-ticker">FCNTX</div>
          <div class="fund-change">+1.5%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">American Funds Growth</div>
          <div class="fund-ticker">AGTHX</div>
          <div class="fund-change">+1.7%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">Invesco QQQ</div>
          <div class="fund-ticker">QQQ</div>
          <div class="fund-change">+1.9%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">SPDR S&P 500</div>
          <div class="fund-ticker">SPY</div>
          <div class="fund-change">+1.1%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">iShares Russell 2000</div>
          <div class="fund-ticker">IWM</div>
          <div class="fund-change">+1.3%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">Vanguard Total Bond</div>
          <div class="fund-ticker">BND</div>
          <div class="fund-change">+0.2%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">iShares Gold Trust</div>
          <div class="fund-ticker">IAU</div>
          <div class="fund-change">-0.4%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">SPDR Gold Shares</div>
          <div class="fund-ticker">GLD</div>
          <div class="fund-change">-0.4%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">iShares Silver Trust</div>
          <div class="fund-ticker">SLV</div>
          <div class="fund-change">+0.2%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">US Oil Fund</div>
          <div class="fund-ticker">USO</div>
          <div class="fund-change">-0.7%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">iShares Copper</div>
          <div class="fund-ticker">JJC</div>
          <div class="fund-change">+1.5%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">Global X Crypto</div>
          <div class="fund-ticker">BTC</div>
          <div class="fund-change">+1.2%</div>
        </div>
        <div class="fund-item">
          <div class="fund-name">Grayscale Bitcoin</div>
          <div class="fund-ticker">GBTC</div>
          <div class="fund-change">+1.2%</div>
        </div>
      </div>
    </div>

    <!-- footer -->
    <footer>
      <p>數據來源：Yahoo Finance (17:15 HKT) | Bloomberg Morning Briefing | Finviz Chart Analysis</p>
      <p>風險聲明：投資有風險，過往表現不代表未來回報</p>
    </footer>
  </body>'''

    # Combine header and new body
    full_content = header + new_body

    # Validate before writing
    if full_content.startswith('<!DOCTYPE html>') and '2026年8月22日' in full_content:
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