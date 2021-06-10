signup_html = """
<!DOCTYPE html>   
<html>   
<head>  

<title> SignUp </title>  

</head>    
<body>    
    <h1>Sign up</h1> 
    <form action="" method="post">  
        <p>
            <label for="email">Email : </label>   
            <input type="text" placeholder="Enter Email" name="email" >
        </p>
        <p>  
            <label>Password : </label>   
            <input type="password" placeholder="Enter Password" name="password">
        </p>
        <p>
            <input type="submit">
        </p>
        <p>
            <a href="http://127.0.0.1:5000/login">Log in</a>
        </p>
        <p>
            <a href="http://127.0.0.1:5000/">Home</a>
        </p>

             
    </form>     
</body>     
</html>  
"""

login_html = """
<!DOCTYPE html>   
<html>   
<head>  

<title> Login </title>  

</head>    
<body>    
    <h1>Log in</h1>
    <form action="" method="post">  
        <p>
            <label for="email">Email : </label>   
            <input type="text" placeholder="Enter Email" name="email" >
        </p>
        <p>  
            <label>Password : </label>   
            <input type="password" placeholder="Enter Password" name="password">
        </p>
        <p>
            <input type="submit">
        </p>
        <p>
            <a href="http://127.0.0.1:5000/signup">Sign up</a>
        </p>
        <p>
            <a href="http://127.0.0.1:5000/">Home</a>
        </p>

             
    </form>     
</body>     
</html>  
"""