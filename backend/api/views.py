from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, ProductSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import  User, Product
from rest_framework.response import Response
# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@api_view(["GET"]) 
def get_tracked_products_home(request):  # to get all tracked products by use rin the home page
    user = request.user
    all_products = list(user.tracked_products.all())
    products_serializer = ProductSerializer(all_products, many=True)  # list of dicts each dict represents a product-obj with its attributes as key/values
    return Response({"tracked_products":products_serializer.data})

@api_view(["POST"]) 
def home(request):
    print(f"Post-request-data: {request.data}")
    user = request.user
    context = {}
    url = request.data["url"]  # get url from post-request
    website = "Amazon" if "amazon" in url else "Ebay" if "ebay" in url else None
    
    # A user agent is a string of text that web browsers and other web applications send to servers to identify themselves. It includes details about the software and operating system of the client making the request. 
    user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    ]
    user_agent = random.choice(user_agents)  # randomly choose a agent
    # Specify chrome-driver path and options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless Chrome
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"user-agent={user_agent}")  # set user-agent
    chrome_options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
    chrome_driver_path = "/Users/pravachanpatra/Desktop/chromedriver-mac-arm64/chromedriver"
    service = Service(chrome_driver_path)
    # Initialize the WebDriver for Chrome
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # Navigate to the URL
    driver.get(url)
    # Wait for the element to be present in the DOM
    wait = WebDriverWait(driver, 10)  # 10 seconds timeout
    # Get elements if website is Amazon
    if website == "Amazon":  
        element_title = wait.until(EC.presence_of_element_located((By.ID, "productTitle")))  # extract html-element with id=productTitle
        element_price = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole")))
        title  = element_title.text.strip() 
        price = element_price.text.strip()

        label_elements = driver.find_elements(By.CSS_SELECTOR, ".a-color-secondary.a-size-base.prodDetSectionEntry") 
        value_elements = driver.find_elements(By.CSS_SELECTOR, ".a-size-base.prodDetAttrValue") 
        upc = None
        for i, label_element in enumerate(list(label_elements)):
            if label_element.text.strip() == "UPC":
                upc = list(value_elements)[i].text.strip()
        
        new_product = Product(title=title, price=float(price), UPC=upc, website=website, url=url)
        new_product.save()
        user.tracked_products.add(new_product)
        user.save()
        all_products = list(user.tracked_products.all())
        products_serializer = ProductSerializer(all_products, many=True)  # list of dicts each dict represents a product-obj with its attributes as key/values
        context["tracked_products"] = products_serializer.data            # add to context
        
        print(f"Website: {new_product.website}")
        print(f"Product Title: {new_product.title}")
        print(f"Product Price: ${new_product.price}")
        print(f"Product UPC: {new_product.UPC}")
    if website == "Ebay":
        pass

    driver.quit()
    print(f"Context: {context}")
    return Response(context)

@api_view(["GET"]) 
def view_product(request, pk):
    product = request.user.tracked_products.filter(id=int(pk))[0]
    prod_serializer = ProductSerializer(product)
    return Response({"product":prod_serializer.data})

# TESTING STUFF BELOW
foo_db = ["foo1","foo1","foo1","foo1","foo1" ]
@api_view(["GET"]) # his view function will respond to HTTP GET requests. When a GET request is made to the corresponding URL (e.g., /api/hello-world/), this function will be invoked
def get_foo(request):
    print(f"USER: {request.user}")
    for user in User.objects.all():
        print(user)

    user_serializer = UserSerializer(request.user)
    return Response({'foo_list': foo_db, "user":user_serializer.data["email"]})

@api_view(["POST"]) # his view function will respond to HTTP GET requests. When a GET request is made to the corresponding URL (e.g., /api/hello-world/), this function will be invoked
def create_foo(request):
    print("HELLOasdasdasdasdasdasdasdasdas")
    content = request.data["content"]
    foo_db.append(content)
    return Response({'foo_list': foo_db})
