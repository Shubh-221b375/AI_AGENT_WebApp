document.getElementById('generateBtn').addEventListener('click', async () => {
    const task = document.getElementById('taskInput').value.trim();
    const output = document.getElementById('planOutput');
  
    if (!task) {
      output.textContent = '❗ Please enter a task first.';
      return;
    }
  
    output.textContent = '⏳ Generating plan...';
  
    try {
      const response = await fetch('/api/plan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task }),
      });
  
      const data = await response.json();
      output.textContent = data.plan || '⚠️ No plan returned.';
    } catch (err) {
      console.error(err);
      output.textContent = '❌ Error fetching plan.';
    }
  });
  