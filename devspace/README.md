# DevSpace 🚀

A comprehensive AI/ML, robotics, and distributed systems development environment designed for modern developers building intelligent applications.

## Overview

DevSpace provides a structured, domain-driven architecture that supports:

- **AI/ML Development**: Agents, training, evaluation, and deployment
- **Robotics & Hardware**: Sensor integration, actuator control, and device provisioning
- **Distributed Systems**: Microservices, APIs, and cluster management
- **Data Engineering**: ETL pipelines, data warehousing, and analytics
- **Workflow Automation**: Multi-step processes and background jobs

## Quick Start

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd devspace

# Install dependencies
pip install -e .

# For development
pip install -e .[dev]

# For robotics features
pip install -e .[robotics]

# For ML features
pip install -e .[ml]
```

### Running the Application

```bash
# Start the main application
devspace

# Use the CLI
devspace-cli --help

# Start the HTTP API
python -m app.http.main
```

## Project Structure

```
devspace/
├── app/                    # Core application logic
│   ├── ai/                 # AI/ML components
│   │   ├── actions/        # AI agent actions
│   │   ├── agents/         # AI agents
│   │   ├── evals/          # Model evaluation
│   │   └── trainers/       # Training modules
│   ├── data/               # Data processing
│   │   ├── extractors/     # Data extraction
│   │   └── transformers/   # Data transformation
│   ├── hardware/           # Hardware interfaces
│   │   ├── actuators/      # Physical actuators
│   │   └── sensors/        # Sensor interfaces
│   ├── http/               # HTTP API
│   │   ├── controllers/    # API controllers
│   │   └── routes/         # API routes
│   ├── workflows/          # Multi-step workflows
│   │   ├── ai/            # AI workflows
│   │   └── processes/     # Business processes
│   ├── jobs/               # Background jobs
│   ├── services/           # Internal services
│   └── cli/                # CLI tools
├── data/                   # Data storage (git-ignored)
│   └── models/             # Trained models
├── tests/                  # Test suites
├── docs/                   # Documentation
├── config/                 # Configuration files
├── notebooks/              # Jupyter notebooks
├── scripts/                # Standalone scripts
│   ├── ai/                 # AI-related scripts
│   └── http/               # HTTP server scripts
├── plugins/                # Plugin system
├── bases/                  # Polylith bases (optional)
└── components/             # Polylith components (optional)
```

## Key Features

### AI/ML Capabilities
- **Agent Framework**: Build and deploy AI agents
- **Training Pipeline**: Automated model training and fine-tuning
- **Evaluation Suite**: Comprehensive model evaluation tools
- **MLOps Integration**: Model versioning and deployment

### Robotics & Hardware
- **Sensor Integration**: Support for various sensor types
- **Actuator Control**: Real-time actuator management
- **Device Provisioning**: Automated hardware setup

### Distributed Systems
- **Microservices**: Scalable service architecture
- **API Gateway**: Centralized API management
- **Background Jobs**: Asynchronous task processing
- **Cluster Management**: Multi-node coordination

### Data Engineering
- **ETL Pipelines**: Extract, Transform, Load operations
- **Data Warehousing**: Structured data storage
- **Stream Processing**: Real-time data processing

## Development

### Code Quality

```bash
# Format code
black app/ tests/
isort app/ tests/

# Lint code
flake8 app/ tests/
mypy app/

# Run tests
pytest

# Run tests with coverage
pytest --cov=app
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

## Configuration

Configuration files are located in the `config/` directory:

- `config/settings.py` - Application settings
- `config/database.py` - Database configuration
- `config/ai.py` - AI/ML configuration
- `config/hardware.py` - Hardware configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

For questions and support, please:
- Check the documentation in `docs/`
- Review existing issues
- Create a new issue for bugs or feature requests

---

**DevSpace** - Empowering the next generation of intelligent applications.
