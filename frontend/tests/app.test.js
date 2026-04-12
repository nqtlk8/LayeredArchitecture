// Nhúng hàm từ file app.js vào để test
const { getGreetingMessage } = require('../app');

test('Hàm getGreetingMessage phải trả về đúng chuỗi', () => {
    const result = getGreetingMessage('Thang');
    expect(result).toBe('Hello, Thang! Welcome to CI/CD.');
});