`timescale 1ns/1ps

module multiplier_delayed_tb;

reg [7:0] x0, x1, x2, x3, x4, x5, x6, x7, x8, x9;
reg [7:0] h0, h1, h2, h3, h4, h5, h6, h7, h8, h9;
reg clk, rst;
wire [15:0] y;

multiplier_delayed multiplier_delayed_inst (
    .x0(x0), .x1(x1), .x2(x2), .x3(x3), .x4(x4),
    .x5(x5), .x6(x6), .x7(x7), .x8(x8), .x9(x9),
    .h0(h0), .h1(h1), .h2(h2), .h3(h3), .h4(h4),
    .h5(h5), .h6(h6), .h7(h7), .h8(h8), .h9(h9),
    .y(y),
    .clk(clk), .rst(rst)
);

initial begin
    clk = 0;
    rst = 1;
    x0 = 8'd1; x1 = 8'd2; x2 = 8'd3; x3 = 8'd4; x4 = 8'd5;
    x5 = 8'd6; x6 = 8'd7; x7 = 8'd8; x8 = 8'd9; x9 = 8'd10;
    h0 = 8'd1; h1 = 8'd2; h2 = 8'd3; h3 = 8'd4; h4 = 8'd5;
    h5 = 8'd6; h6 = 8'd7; h7 = 8'd8; h8 = 8'd9; h9 = 8'd10;

    #10 rst = 0;
    #10 clk = 1;
    #10 clk = 0;
    #10;
    $display("y = %d", y);
    #10;
    $finish;
end

always #5 clk = ~clk;

endmodule

