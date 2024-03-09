function overTime(lst){

    const [start, end, rate, overtimeRate] = lst;
    const regularHours = Math.max(0, Math.min(end, 17) - start);
    const overtimeHours = Math.max(0, end -17);

    let totalPay;
    if (start < 17){
        totalPay = regularHours * rate + overtimeHours * rate * overtimeRate + 0.001;
    } else {
        totalPay = (end - start) * rate * overtimeRate;
    }

    return `$${totalPay.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',')}`;
}

// 使用例
console.log(overTime([9, 17, 30, 1.5]));       // 出力: $240.00
console.log(overTime([16, 18, 30, 1.8]));      // 出力: $54.00
console.log(overTime([13.25, 18, 30, 1.5]));   // 出力: $209.63