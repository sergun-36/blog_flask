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
        <p>
            <a href="http://127.0.0.1:5000/cabinet">Cabinet</a>
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
        <p>
            <a href="http://127.0.0.1:5000/cabinet">Cabinet</a>
        </p>
             
    </form>     
</body>     
</html>  
"""

cabinet_html = """
<!DOCTYPE html>   
<html>   
<head>  

<title>Cabinet</title>  

</head>    
<body>    
    <h1>Cabinet</h1> 
    <form action="" method="post">  
        <p>
            <label for="title">Title : </label>   
            <input type="text" placeholder="Enter Title" name="title" >
        </p>
        <p>  
            <p>Text : </p>   
            <textarea placeholder="Enter Text" name="text" rows="10" cols="45"></textarea>
        </p>
        <p>
            <input type="submit">
        </p>

        <p>
            <a href="http://127.0.0.1:5000/">Home</a>
        </p>
        <p>
            <a href="http://127.0.0.1:5000/login">Log in</a>
        </p>
        <p>
            <a href="http://127.0.0.1:5000/signup">Sign up</a>
        </p>

             
    </form>     
</body>     
</html>  
"""