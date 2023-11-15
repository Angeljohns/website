function validate()
{
var name = document.myForm.mobnu.value;
var mobileRegex = /^[6-9]\d{9}$/; 
if (name == "" || name == null) {
alert("Enter Mobile Number");
var firstNameField = document.getElementById("mobnu");
firstNameField.focus();
return false;
}
else if (!mobileRegex.test(name))
{  
alert("Enter valid Mobile Number");
var firstNameField = document.getElementById("mobnu");
firstNameField.focus();
return false;
}
alert("Registration successful!");
return true;
}
