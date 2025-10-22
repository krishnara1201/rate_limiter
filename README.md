# Rate Limiter

A custom implementation of a rate limiter for controlling the rate of requests/operations.

## Overview

This project implements various rate limiting algorithms to help control the flow of requests in applications. Rate limiting is a crucial technique for:

- **API Protection**: Preventing abuse and ensuring fair usage of API endpoints
- **Resource Management**: Protecting backend services from being overwhelmed
- **Quality of Service**: Ensuring system stability and reliability
- **Cost Control**: Preventing excessive usage that could lead to high costs

## Features

### Planned Rate Limiting Algorithms

- **Token Bucket**: Allows bursts of traffic while maintaining an average rate
- **Leaky Bucket**: Smooths out bursts and processes requests at a constant rate
- **Fixed Window**: Simple counter-based limiting within fixed time windows
- **Sliding Window**: More accurate rate limiting using sliding time windows
- **Sliding Window Log**: Precise request tracking with timestamp-based windows

## Getting Started

### Prerequisites

- Go 1.19 or higher (if implementing in Go)
- Basic understanding of rate limiting concepts

### Installation

```bash
# Clone the repository
git clone https://github.com/krishnara1201/rate_limiter.git

# Navigate to the project directory
cd rate_limiter

# Install dependencies (once implemented)
go mod download
```

## Usage

_Usage examples will be added as the implementation progresses._

```go
// Example usage will be documented here
```

## Rate Limiting Concepts

### Token Bucket Algorithm
The token bucket algorithm works by:
1. Maintaining a bucket with a maximum capacity of tokens
2. Tokens are added to the bucket at a fixed rate
3. Each request consumes one or more tokens
4. If insufficient tokens are available, the request is rejected or delayed

### Leaky Bucket Algorithm
The leaky bucket algorithm:
1. Processes requests at a constant rate
2. Incoming requests are added to a queue (bucket)
3. Requests "leak" out of the bucket at a fixed rate
4. If the bucket is full, new requests are rejected

### Fixed Window Algorithm
Simple time-based counting:
1. Divides time into fixed windows (e.g., 1 minute)
2. Counts requests in each window
3. Resets counter at the start of each new window

### Sliding Window Algorithm
More accurate than fixed window:
1. Uses a rolling time window
2. Calculates rate based on both current and previous windows
3. Provides smoother rate limiting without reset spikes

## Project Structure

```
rate_limiter/
├── README.md           # This file
└── (implementation files will be added)
```

## Roadmap

- [ ] Implement Token Bucket algorithm
- [ ] Implement Leaky Bucket algorithm
- [ ] Implement Fixed Window algorithm
- [ ] Implement Sliding Window algorithm
- [ ] Add unit tests
- [ ] Add benchmarks
- [ ] Add usage examples
- [ ] Add API documentation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by common rate limiting implementations in production systems
- Reference implementations from various open-source projects

## Contact

Project Link: [https://github.com/krishnara1201/rate_limiter](https://github.com/krishnara1201/rate_limiter)

## Resources

- [Rate Limiting Fundamentals](https://en.wikipedia.org/wiki/Rate_limiting)
- [Token Bucket Algorithm](https://en.wikipedia.org/wiki/Token_bucket)
- [Leaky Bucket Algorithm](https://en.wikipedia.org/wiki/Leaky_bucket)
