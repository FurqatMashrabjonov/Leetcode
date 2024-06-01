var titleToNumber = function(columnTitle) {
  let k = 64;
  let columnNumber = 0;
  for (let i = 0; i < columnTitle.length; i++) {
    columnNumber += ((columnTitle.charCodeAt(i) - k) * Math.pow(26,columnTitle.length - i - 1));
  }
  return columnNumber;
};

