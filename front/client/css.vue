<template></template>
<script></script>
<style>
	#main-contaniner {position: relative;	top: 7.5rem;}
	#main-contaniner textarea {margin-left: 0.5rem; margin-right: 0.5rem;}
	#writing-box {
		display: grid;
		top: 20px;
		width: 42.5rem;
		border: 2px solid #C4C4C4;
		margin: 0 auto;
	}
	input:focus, textarea:focus { outline:none;}
	#writing-box textarea.autosize { min-height: 50px; }
	#writing-box #maintext-box {
		border: none;
		resize: none;
		/* overflow-y: hidden; */
	}
	#main-contaniner #writing-box-footer {
		width: 42.5rem;
		margin: 0 auto;
	}
	#writing-box-footer #public-checkbox {
		margin: 5px 0 0;
	}
	#writing-box-footer #public-checkbox #public:focus, #public:active {outline: none !important; box-shadow: none !important; border-color: #C4C4C4; fill: #C4C4C4}
	#writing-box-footer #public-checkbox .form-check-input:checked{background-color: #C4C4C4; border-color: #C4C4C4;}
	#writing-box-footer #public-checkbox .form-check-input:focus{
		background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='rgba%280, 0, 0, 0.25%29'/%3e%3c/svg%3e");
	}
	#writing-box-footer #button-submit {
		display: block;
		border: 0.125rem solid #C4C4C4;
		border-radius: 5px;
		background: #C4C4C4;
		color: #FFF;
		font-size: 1.5rem;
		margin: 5px auto;
		width: 9.375rem;
		height: 3.5rem;
	}
	#writing-box-footer #button-submit:disabled {
		background: #FFFFFF;
		color: #C4C4C4;
	}
	#writing-box-footer #button:active { opacity: 0.5; border: 0.0625rem solid #AFAFAF;}
	.form-switch .form-check-input {
		vertical-align: middle;
    width: 3em;
    height: 1.5em;
		margin-top: 1.5px;
	}
	.form-switch .form-check-label {
		font-size: 1.15rem;
		margin: 0 0 0 0.5rem;
	}
</style>