
  let currentStage = 1;
  const totalStages = 6;

  const ctx = document.getElementById('progress-pie').getContext('2d');
  const progressPie = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Completed', 'Remaining'],
      datasets: [
        {
          data: [1, 5], // Initial data
          backgroundColor: ['#007bff', '#e9ecef'],
        },
      ],
    },
    options: {
      responsive: true,
      cutout: '80%',
      plugins: {
        tooltip: { enabled: false },
        legend: { display: false },
      },
    },
  });

  function moveStage(direction) {
    const nextStage = currentStage + direction;
    if (nextStage >= 1 && nextStage <= totalStages) {
      currentStage = nextStage;
      updateForm();
    }
  }

  function goToStage(stage) {
    currentStage = stage;
    updateForm();
  }

  function updateForm() {
    for (let i = 1; i <= totalStages; i++) {
      const stageElement = document.getElementById('stage' + i);
      const sidebarElement = document.getElementById('stage' + i + '-sidebar');
      if (i === currentStage) {
        stageElement.classList.add('active');
        sidebarElement.classList.add('active');
      } else {
        stageElement.classList.remove('active');
        sidebarElement.classList.remove('active');
      }
    }
    const submitButton = document.getElementById('submit-btn');
    if (currentStage === totalStages) {
      submitButton.style.display = 'inline-block';
    } else {
      submitButton.style.display = 'none';
    }
    updateProgressPie();
  }

  function updateProgressPie() {
    const completed = currentStage;
    const remaining = totalStages - currentStage;
    progressPie.data.datasets[0].data = [completed, remaining];
    progressPie.update();

    const progressText = document.getElementById('progress-text');
    progressText.textContent = `Stage ${currentStage} of ${totalStages}`;
  }

  updateForm();

