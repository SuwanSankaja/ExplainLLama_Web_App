# Use the official Node.js image
FROM node:18-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json /app/
RUN npm install

# Copy the React app into the container
COPY . /app/

# Build the React app for production
RUN npm run build

# Serve the app using a simple HTTP server
RUN npm install -g serve

# Expose the port that the app will run on
EXPOSE 3000

# Start the app using serve
CMD ["serve", "-s", "build"]
