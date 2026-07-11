## Scalable REST API Automation Framework with Python, Pytest, Requests
- create virtual enviorment - python -m venv .venv
- to activate virtual env on window - .venv\Scripts\activate
- to fix error execute below command
 Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1


##### Plawright-Pytest-Automation-Framework/

### Available Scopes
#### You can configure the scope by passing the scope parameter to the 
####  @pytest.fixture decorator. There are five available scopes

##### 1. function: Default scope. Created and destroyed for each test function.
##### 2. class: Created once per test class. Shared among all test methods in that class.
##### 3. module: Created once per Python file (module). Shared among all tests in that file.
##### 4. package: Created once per test package (directory). Shared across multiple modules inside that directory.
##### 5. session: Created once per entire test run. Shared globally across all test files.
