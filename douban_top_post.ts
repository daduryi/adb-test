import * as puppeteer from 'puppeteer';
import * as Tesseract from 'tesseract.js';

const log = console.log;

/**
 * h5站外风享页
 * 次数多了有验证码, nodejs没有找到好用的解析工具, python应该有.
 */
class DoubanPuppeteer {

  browser: puppeteer.Browser;
  urls: string[];
  pages: puppeteer.Page[] = [];

  constructor(urls: string[]) {
    this.urls = urls;
  }

  async launch() {
    this.browser = await puppeteer.launch({
      headless: false,
      slowMo: 250,
      devtools: true
    });
  }

  async openPages() {
    for (const url of this.urls) {
      log(url);
      const page = await this.browser.newPage();
      await page.goto(url);
      this.pages.push(page);
    }
  }

  async reply() {
    for (const page of this.pages) {
      log('reply');
      const input_area = await page.$("#last");
      await input_area.type("1");
      const btn = await page.$("input[name='submit_btn']");
      btn.click();
      await sleep(random_s(60*10, 60*15));
    }
  }

  async button_continue_reply() {
    for (const page of this.pages) {
      log('continue button');
      const btn = await page.$("#last");
      btn.click();
      await sleep(random_s(1, 10));
    }
  }
}

async function sleep(ms) {
  log('sleep ' + Math.floor(ms / 1000) + 's');
  return new Promise(resolve => {
    setTimeout(resolve, ms);
  });
}

function random_s(s1: number, s2: number) {
  return (Math.random() * (s2 - s1) + s1) * 1000; 
}

async function main() {
  const urls = [
    'https://www.douban.com/group/topic/158250561/?dt_platform=com.douban.activity.wechat_friends&dt_dapp=1',
    // 'https://www.douban.com/group/topic/158250646/?dt_platform=com.douban.activity.wechat_friends&dt_dapp=1',
    'https://www.douban.com/group/topic/158250717/?dt_platform=com.douban.activity.wechat_friends&dt_dapp=1',
    'https://www.douban.com/group/topic/158250807/?dt_platform=com.douban.activity.wechat_friends&dt_dapp=1'
  ]
  const pupter = new DoubanPuppeteer(urls)
  await pupter.launch();
  await pupter.openPages();
  await sleep(30000);
  log('end');

  let count = 0;

  while(true) {
    count++;
    log('reply count ' + count);
    await pupter.reply();
    await sleep(random_s(2,5));
    await pupter.button_continue_reply();
    // const _time = random_s(3 * 60, 10 * 60)
    // await sleep(_time);
  }
}

if (!module.parent) {
  main();
}