#!/usr/bin/node
const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  let first = parseInt(args[2]);
  let second;
  if (parseInt(args[3]) > first) {
    second = first;
    first = parseInt(args[3]);
  } else { second = parseInt(args[3]); }

  for (let i = 4; i < args.length; i++) {
    const next = parseInt(args[i]);
    if (next > first) {
      second = first;
      first = next;
    } else if (next > second) {
      second = next;
    }
  }
  console.log(second);
}
