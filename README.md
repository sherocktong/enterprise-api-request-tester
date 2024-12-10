# Enterprise API Request Tester 🚀🔍

![Enterprise API Request Tester](finished_ui.PNG)

## Table of Contents 📚
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview 🌟

The Enterprise API Request Tester is a powerful, user-friendly tool designed for developers, QA engineers, and API enthusiasts. It allows users to easily construct, send, and analyze HTTP requests to any API endpoint. With a sleek interface and robust functionality, this tool streamlines the process of API testing and exploration.

## Features 💡

- **Multiple HTTP Methods** 🔄: Support for GET, POST, PUT, DELETE, PATCH, HEAD, and OPTIONS.
- **Custom Headers** 📝: Add and modify request headers with ease.
- **Request Body Editor** ✏️: Built-in editor for crafting JSON request bodies.
- **Authentication Support** 🔐: Includes options for Bearer Token and Basic Auth.
- **Response Viewer** 👀: Clear display of API responses with options for raw and formatted views.
- **Request Saving** 💾: Save and manage frequently used API requests.
- **Import/Export** 📤📥: Share your API collections with team members.
- **Sample Requests** 🧪: Quick-load sample requests using real, functional APIs for instant testing.
- **Responsive Design** 📱💻: Seamless experience across desktop and mobile devices.
- **CORS-Friendly** 🌐: Built-in proxy to handle CORS issues, allowing testing of various APIs.
- **Error Handling** 🐛: Comprehensive error handling and display for better debugging.
- **Timeout Management** ⏱️: Implements request timeouts to prevent long-running requests.

## Tech Stack 🛠️

- **Frontend Framework**: Typescript with Next.js (App Router) ⚛️
- **UI Components**: shadcn/ui 🎨
- **Styling**: Tailwind CSS 💅
- **State Management**: WebHooks (useState, useEffect) 🎣
- **HTTP Requests**: Fetch API with custom proxy implementation 🌐
- **Animations**: Framer Motion 🎬
- **Notifications**: Hot Toast 🍞
- **Icons**: Lucide React 🖼️
- **Language**: TypeScript 📘
- **Deployment**: Vercel-ready 🚀

## Getting Started 🏁

### Prerequisites 📋

- Node.js (v14.0.0 or later) 📦
- npm or yarn 🧶

### Installation

1. Clone the repository:

```bash
   git clone https://github.com/sherocktong/enterprise-api-request-tester.git
```

2. Navigate to the project directory:

```shellscript
cd enterprise-api-request-tester
```


3. Install dependencies:

```shellscript
npm install
# or
yarn install
```


4. Start the development server:

```shellscript
npm run dev
# or
yarn dev
```


5. Open [http://localhost:3000](http://localhost:3000) in your browser to see the application.


## Usage 🚀

1. **Select HTTP Method** 🔄: Choose from GET, POST, PUT, DELETE, PATCH, HEAD, or OPTIONS.
2. **Enter URL** 🔗: Input the API endpoint URL you want to test.
3. **Add Headers** 📝: (Optional) Add any custom headers required for your request.
4. **Add Body** 📦: (Optional) For methods like POST or PUT, add a JSON body to your request.
5. **Set Authentication** 🔐: (Optional) Configure Bearer Token or Basic Auth if required.
6. **Send Request** ▶️: Click the "Send Request" button to make the API call.
7. **View Response** 👀: Analyze the API response in the response viewer.
8. **Save Request** 💾: (Optional) Save your request for future use.
9. **Load Sample** 🧪: Use the "Load Sample" button to quickly test with pre-configured, functional API requests.

---
## Generate import files from Postman requests
1. Converting postman request HTTP code snippets into the requests, so that you can use postman to edit requests and convert them to the requests to run on next.js.

2. Create a folder with a name of site ID under source folder. The site ID is creator ID.

3. Create a file with a meaningful request name under directory `${project}/source/${site-id}/`. The file name is also the request name, so I recommend to create the names with no extension names. For example, for the above code snippet, I suggest to set the file name as "group-list".

4. Follow the [guide](https://learning.postman.com/docs/sending-requests/create-requests/generate-code-snippets/) to get HTTP code snippets. You may get a code snippet like this:
```
GET /serve-lab/group/groups?size=20&sortBy=createdAt&sortDirection=asc&groupName=&start=1 HTTP/1.1
Host: test-site-id-ms.testdomain.com
```

5. Past the snippet into the file just created. **DO NOT modify** anything manually to the snippet.

6. Navigate to project root directory and run `python3 convert.py`. There is a json file named as site ID created under target directory. It is not particular for Python's version. The Python I use is 3.11.

7. Now follow the [installation](#installation) guide to start up this tool, and import the json file from UI.

---
## Contributing 🤝

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project 🍴
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`) 🌿
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`) 💬
4. Push to the Branch (`git push origin feature/AmazingFeature`) 🚀
5. Open a Pull Request 🎉

## License 📄

Distributed under the MIT License. See `LICENSE` for more information.

## Contact 📬

Sunny Patel - [sunnypatel124555@gmail.com](mailto:sunnypatel124555@gmail.com)

Project Link: [https://github.com/your-username/enterprise-api-request-tester](https://github.com/your-username/enterprise-api-request-tester)

---

Made by [Sunny Patel](https://www.sunnypatel.net/)
---
