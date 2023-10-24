// 1-stdin.js
process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.setEncoding('utf8');
process.stdin.on('readable', () => {
  const tunombre = process.stdin.read();
  if (tunombre !== null) {
    process.stdout.write(`Your name is: ${tunombre}`);
  }
});

  process.stdin.on('end', () => {
    process.stdout.write('This important software is now closing\n');
});
