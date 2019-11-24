import * as Tesseract from 'tesseract.js'

// Tesseract.recognize('./captcha.jpeg',
//   'eng',
//   { logger: m => console.log(m) }
// ).then(({ data: { text } }) => {
//   console.log(text);
// })

/**
 * 测试node tesseract 模块文字识别
 * 这是只是一个文字识别, 算不上验证码识别
 */

Tesseract.recognize(
  // 'https://tesseract.projectnaptha.com/img/eng_bw.png',
  // './captcha.jpeg',
  './text.png',
  { logger: m => console.log(m) }
).then((data: any) => {
  // console.log(data.data.text);
  console.log(data.text);
})