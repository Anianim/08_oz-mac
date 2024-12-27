document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    const confirmPassword = document.getElementById('confirmPassword').value.trim();
    const name = document.getElementById('name').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const gender = document.querySelector('input[name="gender"]:checked').value;
    const email = document.getElementById('email').value.trim();

    /* 유효성 검사 */
    if (username.length < 4) {
        alert('아이디는 4자 이상이어야 합니다.');
        return;
    }
    if (password.length < 8 || password.length >= 30 || !/[A-Za-z]/.test(password) || !/[0-9]/.test(password) || !/[!@#$%^&*]/.test(password)) {
        alert('비밀번호는 영문, 숫자, 특수문자를 포함한 8자 이상 30자 미만이어야 합니다.');
        return;
    }
    if (password !== confirmPassword) {
        alert('비밀번호가 일치하지 않습니다.');
        return;
    }
    if (!name) {
        alert('이름을 입력하세요.');
        return;
    }
    if (!/^\d+$/.test(phone)) {
        alert('전화번호는 숫자만 입력할 수 있습니다.');
        return;
    }
    if (!email) {
        alert('이메일 주소를 입력하세요.');
        return;
    }
    /* 가입완료 안내 */  
    alert(`가입 축하드립니다!\n 이름: ${name}님 `);

    /* 가입 완료후 리디렉션 */
    location.href = "redirect_join.html";
    });