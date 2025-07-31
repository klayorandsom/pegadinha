<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Você me ama?</title>
  <style>
    body {
      background: #ffe6f0;
      font-family: 'Comic Sans MS', cursive, sans-serif;
      text-align: center;
      padding-top: 50px;
      user-select: none;
    }
    h1 {
      color: #ff007f;
      font-size: 2.5em;
    }
    button {
      font-size: 1.5em;
      padding: 15px 40px;
      margin: 20px;
      border: none;
      border-radius: 12px;
      cursor: pointer;
      transition: background-color 0.3s;
      position: absolute;
    }
    #sim {
      background-color: #90ee90;
      color: #006400;
      left: 30%;
      top: 50%;
      transform: translate(-50%, -50%);
    }
    #sim:hover {
      background-color: #32cd32;
    }
    #nao {
      background-color: #ff9999;
      color: #8b0000;
      top: 50%;
      left: 70%;
      transform: translate(-50%, -50%);
    }
    #nao:hover {
      background-color: #ff4d4d;
    }
  </style>
</head>
<body>

  <h1>Você me ama?</h1>
  <button id="sim">Sim ❤️</button>
  <button id="nao">Não 💔</button>

  <script>
    const nao = document.getElementById('nao');
    let larguraTela = window.innerWidth;
    let alturaTela = window.innerHeight;

    function fugir() {
      const maxX = larguraTela - nao.offsetWidth - 20;
      const maxY = alturaTela - nao.offsetHeight - 20;

      const novaX = Math.floor(Math.random() * maxX);
      const novaY = Math.floor(Math.random() * maxY);

      nao.style.left = novaX + 'px';
      nao.style.top = novaY + 'px';

      const cores = ['#ff4d4d', '#ff1a1a', '#e60000', '#cc0000', '#b30000'];
      nao.style.backgroundColor = cores[Math.floor(Math.random() * cores.length)];
    }

    nao.addEventListener('mouseenter', fugir);
    nao.addEventListener('click', (e) => {
      e.preventDefault();
      fugir();
    });

    document.getElementById('sim').addEventListener('click', () => {
      alert('Eu sabia que você me ama! ❤️😘');
    });

    window.addEventListener('resize', () => {
      larguraTela = window.innerWidth;
      alturaTela = window.innerHeight;
    });
  </script>

</body>
</html>
