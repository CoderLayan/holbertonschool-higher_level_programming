# Basics of HTTP/HTTPS

## HTTP (HyperText Transfer Protocol)
- **Definition**: HTTP is a protocol used for transmitting hypertext over the internet. It is the foundation of any data exchange on the Web and is used for fetching resources such as HTML documents.
- **Port**: Typically uses port 80.
- **Security**: Data is transmitted in plain text, making it vulnerable to interception and attacks. Any data sent over HTTP can be read by anyone who intercepts the communication.
- **Use Case**: Suitable for non-sensitive data transmission where security is not a primary concern. Commonly used for informational sites or blogs.

## HTTPS (HyperText Transfer Protocol Secure)
- **Definition**: HTTPS is an extension of HTTP that uses encryption to secure data transmission. It ensures that data sent between the client and server is encrypted and secure from eavesdroppers.
- **Port**: Typically uses port 443.
- **Security**: Data is encrypted using SSL/TLS, providing confidentiality, integrity, and authentication. Even if the data is intercepted, it cannot be read without the decryption key.
- **Use Case**: Essential for transmitting sensitive data such as login credentials, payment information, and personal details. Used by secure websites such as online banking and e-commerce platforms.

### Key Differences
1. **Security**: HTTP is not secure, while HTTPS provides encrypted and authenticated communication.
2. **Port**: HTTP uses port 80, whereas HTTPS uses port 443.
3. **Encryption**: HTTP transmits data in plain text; HTTPS encrypts data using SSL/TLS.
4. **Trust**: HTTPS requires a digital certificate from a trusted Certificate Authority (CA).

---

## HTTP/2 Request and Response Structure

### HTTP/2 Request
An HTTP/2 request consists of the following components:
- **:method**: The HTTP method (e.g., GET, POST).
- **:scheme**: The scheme of the target URL (e.g., https).
- **:authority**: The authority of the target URL (e.g., www.example.com).
- **:path**: The path of the target URL (e.g., /index.html).
- **Headers**: Metadata about the request (e.g., User-Agent, Accept).
- **Body**: Payload of the request (used with POST, PUT, etc.).

#### Example:
```
:method: GET
:scheme: https
:authority: www.example.com
:path: /index.html
user-agent: Mozilla/5.0
accept: text/html
```

### HTTP/2 Response
An HTTP/2 response consists of the following components:
- **:status**: The HTTP status code (e.g., 200, 404).
- **Headers**: Metadata about the response (e.g., Content-Type).
- **Body**: The content returned in the response.

#### Example:
```
:status: 200
content-type: text/html
content-length: 1234

<html>
    <body>
        <h1>Hello, World!</h1>
    </body>
</html>
```

### Key Features of HTTP/2
1. **Multiplexing**: Multiple requests and responses can be sent simultaneously over a single connection.
2. **Header Compression**: Uses HPACK to compress headers and reduce overhead.
3. **Stream Prioritization**: Allows clients to prioritize important resources.
4. **Server Push**: Servers can send resources proactively before the client requests them.

---

## Common HTTP Methods

### GET
- **Description**: Retrieves data from the server.
- **Use Case**: Fetching a web page or API data.

### POST
- **Description**: Submits data to a specified resource for processing.
- **Use Case**: Form submissions, uploading files.

### PUT
- **Description**: Updates an existing resource with new data.
- **Use Case**: Updating user profiles or data records.

### DELETE
- **Description**: Deletes a specified resource.
- **Use Case**: Removing an item or account.

### PATCH
- **Description**: Partially modifies a resource.
- **Use Case**: Updating specific fields, like changing a user's email.

### HEAD
- **Description**: Similar to GET, but only retrieves headers.
- **Use Case**: Check if a resource exists or is updated without downloading it.

### OPTIONS
- **Description**: Returns the communication options for a resource.
- **Use Case**: Discovering supported HTTP methods.

### CONNECT
- **Description**: Establishes a tunnel to a server, often for SSL.
- **Use Case**: Used in HTTPS through a proxy.

### TRACE
- **Description**: Echoes the received request for testing/debugging.
- **Use Case**: Diagnosing path to the server.

---

## Common HTTP Status Codes

### 200 OK
- **Description**: Request was successful.
- **Scenario**: Web page loads successfully.

### 201 Created
- **Description**: Request succeeded and a resource was created.
- **Scenario**: User registration or new item creation.

### 204 No Content
- **Description**: Request succeeded but no content is returned.
- **Scenario**: After a successful DELETE request.

### 400 Bad Request
- **Description**: Server couldn’t understand the request due to invalid syntax.
- **Scenario**: Missing or incorrect parameters.

### 401 Unauthorized
- **Description**: Authentication is required.
- **Scenario**: Accessing a protected resource without logging in.

### 403 Forbidden
- **Description**: Client does not have access rights.
- **Scenario**: Trying to access restricted content.

### 404 Not Found
- **Description**: The requested resource couldn’t be found.
- **Scenario**: Non-existent URL.

### 500 Internal Server Error
- **Description**: Generic server error.
- **Scenario**: Unhandled exception or issue on server side.

### 502 Bad Gateway
- **Description**: Server received an invalid response from upstream.
- **Scenario**: Issues with another server in a proxy setup.

### 503 Service Unavailable
- **Description**: Server is currently unable to handle the request.
- **Scenario**: Server is down or undergoing maintenance.

