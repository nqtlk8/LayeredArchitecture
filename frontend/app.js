// Một hàm logic đơn giản trên FE để tạo câu chào
function getGreetingMessage(name) {
    return `Hello, ${name}! Welcome to CI/CD.`;
}

// Xuất hàm ra để file test có thể đọc được
module.exports = { getGreetingMessage };